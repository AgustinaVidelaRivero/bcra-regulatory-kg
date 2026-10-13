# U-SEG-OFICIAL — REPORTE de S1-quater, sorteo (13/10/2026)

El paso 3 del §9 del diseño de S1-quater, en sus tres primeros puntos: las poblaciones (versión 5, adenda 4), la regresión y el
sorteo con el orden. Cada salida quedó sellada antes de correr la siguiente. USD 0, sin API. Ningún id ni texto de unidades en este
archivo ni en `s1quater/sorteo/`: las cuatro salidas con ids son archivos `NO_ABRIR_` del paquete, fuera del repo, escritas por los
scripts. De las unidades, mis comandos imprimieron solo sha256, cuentas, horas y nombres de documento. La salida de los tres scripts
del diseño y la de mis controles de los pasos 2 a 4 pasaron por un filtro que reemplaza lo que tenga forma de id
(`<documento>::…`) por «un id», y el filtro no reemplazó nada. Las fichas y los controles a ciegas son de un despacho posterior.

## 1. Qué rige y con qué entradas

- **Diseño y adendas,** en HEAD (`git show HEAD:… | shasum -a 256`), los cinco con el sha256 del despacho: `diseno_S1quater.md`
  `e4193377…`, `adenda_1` `8ce0ad8b…`, `adenda_2` `176fcd4d…`, `adenda_3` `16b36464…`, `adenda_4` `65dcc263…`.
- **Scripts del diseño,** copiados de HEAD (`git show HEAD:…`) a `<scratchpad>/scripts_s1quater/`, desde donde corrieron:
  `poblaciones_S1quater_v5.py` `23676128…`, `comun_S1quater.py` `ade9df93…`, `regresion_S1quater.py` `5c1ebe63…` y
  `sorteo_S1quater.py` `9def8fed…`. Los cuatro dan el sha256 del despacho. Antes de leerlos conté sus líneas con `::`: ninguna trae
  un id, todas son código (`split("::")`, `RE_PARTE`).
- **Paquete de la mesa:** de los seis archivos del despacho controlé el sha256 con `shasum -a 256 -c`, sin abrirlos: los seis dan
  OK. Solo los pasé como argumentos. Del paquete no leí ni listé nada más.
- **Insumos de S1-ter en la copia:** `s1ter/manifest_salida.json` `5e63dff2…`, `s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`
  `f59cdea0…` y `s1ter/tramo_b/orden_lectura_S1ter.json` `acd57e37…`. Los tres son iguales a HEAD y a las constantes de
  `comun_S1quater.py`. `s1ter/e0/`, que no está en git, tiene 768 archivos en el repo y 768 en la copia, y los scripts lo
  controlan contra `manifest_salida.json`.
- **Python:** 3.10.13, el del `.venv` del repo, siempre con `-B` y `PYTHONDONTWRITEBYTECODE=1`.

## 2. Paso 1: la E0 de 2374968a, en una copia

- **La copia:** `rsync -a --no-links --exclude=/.git --exclude=/.venv <repo>/ <scratchpad>/copia_repo/`, de 09:49:52 a 09:50:30,
  con rc 0. Quedan 0 enlaces en la copia y 26.451 archivos.
  - rsync salteó 339 enlaces simbólicos: 336 de `data/experiment/ev2_corrida/navegabilidad/trazas_nav/` y 3 de `.venv-app/bin/`.
  - Ninguno es insumo de E0 ni de S1-quater.
- **La raíz mínima:** `zsh <copia>/…/s0_4/scripts/raiz_minima.sh <copia> <scratchpad>/raiz_minima
  <copia>/data/experiment/reextraccion_v2/e0_chunking`, con rc 0 y 0 enlaces.
  - Código de E0 en la raíz: `e0_lib.py` `d89aab1a…`, `correr_e0.py` `78c54c4c…`, `selftest_e0.py` `eb4f11e6…` y `e0_tablas.py`
    `ab300a22…`.
  - Son los de `codigo_sha256` del manifiesto de S0-6b y los de `s0_6/bis/parche/LEEME.md`.
- **La corrida:** `<copia>/…/s0_1/scripts/correr_152.py --codigo <raíz> --salida <scratchpad>/e0_152 --workers 8`, de 09:50:45 a
  09:54:53, con rc 0: «listo 152 TOs, 0 con error», 0 líneas `ERROR` y 769 entradas (los 768 archivos más `por_to/`).
- **El control** (`scripts/control_e0_S1quater_sorteo.py`; `controles/control_e0_S1quater_sorteo.json`, 09:55:11):
  - el manifiesto `s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json` da `80adbd58…`, el del despacho;
  - están sus 768 archivos `e0/…`, sin faltantes ni sobrantes, y todos dan su sha256;
  - hay 152 TOs y **10.478 unidades**, con 0 TOs cuya cuenta difiera de `unidades_por_to`.
  - S0-6b corrió con 9 workers y yo con 8: la salida es igual archivo por archivo.
- **La E0 no se guarda:** no va al paquete. Queda solo en el scratchpad de la sesión, que el limpiador temporal de macOS borra (CLAUDE.md §4.g).

## 3. Paso 2: las poblaciones

- **Comando:** `poblaciones_S1quater_v5.py`, con los argumentos del despacho (§6), de 09:55:31 a 09:55:36, con rc 0.
- **Salida:** `NO_ABRIR_poblaciones_S1quater.json` `f77bf6adc34d9258ed80edd5e4a7ba6e97ae052c814cd156ea20ccdc743faed5`.
  Sello: `sello_poblaciones_S1quater.txt`, 09:55:48.
- **Control en cuentas** (`scripts/control_poblaciones_S1quater_sorteo.py`; `controles/control_poblaciones_S1quater_sorteo.json`).
  Recalcula el sha256 de los ids ordenados de cada estrato y lo compara con el del JSON y con el del despacho:

  | estrato | unidades | sha256 de los ids ordenados | documentos | peso |
  |---|---|---|---|---|
  | vigente | 6.746 | `e6ebad8abe0fe88c3a8f75026f12074d10c031a9766f0863242b7904ec843758` | 91 | 0,8728 |
  | marcadores | 86 | `dea0af647f282d675b0a201a119d69240775eaf1653f18a42480e9cf5d9d553b` | 5 | 0,0111 |
  | sin_raiz | 897 | `6752a7205f4ce83f5e77a10b423dccd98827acf142b0b7043a846105a14a7078` | 43 | 0,1161 |
  | total | 7.729 | | 139 | 1 |

  - **Coinciden con el despacho:** los tres estratos, en unidades y en sha256.
  - **Consistencia:** los estratos no comparten unidades; la población y las listas de salida son disjuntas; ninguna unidad se
    repite entre listas.
- **Salen 2.609 unidades** (684 + 331 + 10 + 606 + 978), por motivo y estrato (vigente / marcadores / sin_raiz):
  - por construcción, 684 (671 / 0 / 13);
  - por leídas en S1-ter, 331 (193 / 15 / 123);
  - por diseño de S0-6a, 10 (0 / 0 / 10);
  - por la adenda 3, 606 (190 / 17 / 399);
  - por la adenda 4, 978 (460 / 82 / 436). Es la cifra de la adenda 4, §3, estrato por estrato. 8 de estas 978 traen
    `solapa_sin_orden`.
- **Las listas de entrada, como las declaran el JSON y las adendas:**
  - leídas en S1-ter: 286 mostradas;
  - adenda 2: 4;
  - adenda 3: 282 (9 / 5 / 6 / 262);
  - adenda 4: 801 (108 / 5 / 87 / 29 / 93 / 29 / 450 / 0 / 0 / 0, en el orden de la tabla de la adenda 4, §0).
- **ri2_pm, unidades que cruzan fichas:** 0.
- **Cobertura:** de 139 documentos alineados, 4 quedan bajo el umbral 0,95. Ninguno frena: los cuatro van por la exclusión sin
  orden, con las mismas cifras de la adenda 4, §3:

  | documento | cobertura | salen solo por la exclusión sin orden |
  |---|---|---|
  | ri2_ae | 0,660 | 27 |
  | ri_spi | 0,700 | 8 |
  | ri_sef | 0,816 | 2 |
  | ri_ccpnp | 0,897 | 0 |

- **`commit_codigo_e0_corregida`:** el JSON dice «PENDIENTE (lo fija el commit de la autora)», copiado del manifiesto de S0-6b. No
  toqué el JSON.
  - El commit es `2374968a`. Lo declara `s0_6/b/decisiones_adenda_4_y_S0-6b_mesa.md`, §3 («el commit es este»).
  - Ese archivo entró en `2374968a` (`git log --diff-filter=A`), el mismo commit que deja el código de E0 con los sha256 de arriba.

## 4. Paso 3: la regresión

- **Comando:** `regresion_S1quater.py`, con los argumentos del despacho (§6), de 09:56:16 a 09:56:18, con rc 0.
- **Salida:** `NO_ABRIR_regresion_S1quater.json` `57b0436de9a0879773880417282c647e9491482e04d29c08a38f437d95315c87`.
  Sello: `sello_regresion_S1quater.txt`, 09:56:30.
- **Control en cuentas** (`scripts/control_regresion_S1quater_sorteo.py`; `controles/control_regresion_S1quater_sorteo.json`):
  - **la lista:** 60 unidades, ordenadas y sin repetir, con sha256 de los ids ordenados
    `57e904461ab0f5b6cfbc8baae0cac870a2b6ddb92fddc24197cfa2621f7f5cb8`, el del despacho;
  - **los errores confirmados de S1-ter:** 41, todos con unidades. Por origen: 14 por `marca`, 4 por `la_que_sigue` y 23 por
    `herencia`;
  - **las unidades viejas:** 44, de 24 documentos, 2 de ellos bajo el umbral;
  - **sin unidad nueva que las solape:** 3, como prevé el despacho: 2 de un documento con cobertura bajo el umbral y 1 de otro con
    cobertura sobre el umbral. No nombro los documentos;
  - **las unidades nuevas** que salen de las viejas son 60, las de la lista.

## 5. Paso 4: el sorteo y el orden

- **Comando:** `sorteo_S1quater.py`, con `--sha-poblaciones` y `--sha-regresion` tomados de los dos sellos anteriores, a las
  09:56:47, con rc 0.
- **Salidas:**
  - `NO_ABRIR_muestra_S1quater.json` `90ae1225699cec939f05379a9fce3dbdcf44935b2faddc2f156fc431a95470ab`;
  - `NO_ABRIR_orden_lectura_S1quater.json` `b794f85f75a0dc12e5f5b849cc21469358316b8802056a0a3d0c79950cc6431a`;
  - sello: `sello_sorteo_S1quater.txt`, 09:57:01.
- **Control en cuentas** (`scripts/control_sorteo_S1quater_sorteo.py`; `controles/control_sorteo_S1quater_sorteo.json`):
  - **el sorteo rehecho:** el script lo rehace por su cuenta, con las semillas del diseño (§4) y sin importar los scripts del diseño.
    La muestra de cada estrato y el orden de la etapa 1 son iguales a los rehechos;
  - **la muestra:** 40 / 10 / 40, 90 unidades distintas, cada una de la población de su estrato y ninguna de la regresión. sha256 de
    los 90 ids ordenados: `4fe6b0da6d28817a28de2e16970f10a3a5f96e6bb8f07c4069803fba587f08d6`, el mismo en el JSON;
  - **la etapa 1:** 90 fichas, de `E1-001` a `E1-090` sin saltos, con las 90 de la muestra, 40 / 10 / 40 por estrato y la semilla
    del orden `U-SEG-OFICIAL:cortes:S1-quater:orden`;
  - **la etapa 2:** 60 fichas, de `E2-001` a `E2-060` sin saltos, con las 60 de la regresión en el orden de sus ids, cada una con su
    unidad como única calificada.

## 6. Comandos

Las rutas `s0_1/…`, `s0_4/…`, `s0_6/…`, `s1ter/…` y `s1quater/…` son de `segmentacion_oficial_e0r2/`, en la copia.
`<mesa>` es la carpeta `hoja_de_ruta_tanda1_mesa/` del paquete de la mesa que cita el despacho. `<paquete>` es
`revision_USEG_OFICIAL_FRENO_S1quater_sorteo/`, en el scratchpad. `PY` es el `python` del `.venv` del repo, siempre con
`PYTHONDONTWRITEBYTECODE=1` y `-B`.

```
rsync -a --no-links --exclude=/.git --exclude=/.venv <repo>/ <copia>/
zsh <copia>/…/s0_4/scripts/raiz_minima.sh <copia> <raíz> <copia>/data/experiment/reextraccion_v2/e0_chunking
PY -B <copia>/…/s0_1/scripts/correr_152.py --codigo <raíz> --salida <e0> --workers 8
PY -B scripts/control_e0_S1quater_sorteo.py --e0 <e0> --manifest s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json --sha-manifest 80adbd58… --out <json>
PY -B <scratchpad>/scripts_s1quater/poblaciones_S1quater_v5.py --e0-nuevo <e0> --manifest-nuevo s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json --sha-manifest-nuevo 80adbd58… --e0-viejo s1ter/e0 --manifest-viejo s1ter/manifest_salida.json --manifiesto-tos s1ter/manifiesto/segmentacion_oficial_e0r2_152.json --orden-s1ter s1ter/tramo_b/orden_lectura_S1ter.json --diseno-s0-6a <mesa>/revision_FRENO_S0-6a_mesa/adenda_2_S1quater/NO_ABRIR_unidades_diseno_guardas_A_S0-6a.json --adenda-3 <mesa>/preparacion_S0-6a-bis_mesa/adenda_3_S1quater/NO_ABRIR_unidades_adenda_3_S1quater.json --adenda-4 <mesa>/decisiones_S0-6a-bis_y_adenda_4_mesa/adenda_4_S1quater/NO_ABRIR_unidades_adenda_4_S1quater.json --out <paquete>/NO_ABRIR_poblaciones_S1quater.json
PY -B scripts/control_poblaciones_S1quater_sorteo.py --poblaciones <paquete>/NO_ABRIR_poblaciones_S1quater.json --sha f77bf6ad… --out <json>
PY -B <scratchpad>/scripts_s1quater/regresion_S1quater.py --adjudicada-1 <mesa>/adjudicacion_S1ter_cierre_mesa/corrida/planilla_adjudicada_etapa_1_S1ter.tsv --sha-adjudicada-1 1b1d35c0… --adjudicada-2 <mesa>/adjudicacion_S1ter_cierre_mesa/corrida/planilla_adjudicada_etapa_2_S1ter.tsv --sha-adjudicada-2 7c9adf14… --registro-adjudicacion <mesa>/adjudicacion_S1ter_cierre_mesa/corrida/registro_aplicar_adjudicacion_S1ter.json --sha-registro-adjudicacion e4dde326… --orden-s1ter s1ter/tramo_b/orden_lectura_S1ter.json --e0-viejo s1ter/e0 --manifest-viejo s1ter/manifest_salida.json --e0-nuevo <e0> --manifest-nuevo s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json --sha-manifest-nuevo 80adbd58… --out <paquete>/NO_ABRIR_regresion_S1quater.json
PY -B scripts/control_regresion_S1quater_sorteo.py --regresion <paquete>/NO_ABRIR_regresion_S1quater.json --sha 57b0436d… --out <json>
PY -B <scratchpad>/scripts_s1quater/sorteo_S1quater.py --poblaciones <paquete>/NO_ABRIR_poblaciones_S1quater.json --sha-poblaciones f77bf6ad… --regresion <paquete>/NO_ABRIR_regresion_S1quater.json --sha-regresion 57b0436d… --muestra <paquete>/NO_ABRIR_muestra_S1quater.json --orden <paquete>/NO_ABRIR_orden_lectura_S1quater.json
PY -B scripts/control_sorteo_S1quater_sorteo.py --poblaciones … --sha-poblaciones f77bf6ad… --regresion … --sha-regresion 57b0436d… --muestra … --sha-muestra 90ae1225… --orden … --sha-orden b794f85f… --out <json>
find . -path ./.git -prune -o -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 > <foto>     (desde la raíz del repo)
PY -B scripts/comparar_fotos_S1quater_sorteo.py --antes <foto antes> --despues <foto después> --permitido ./data/experiment/segmentacion_oficial_e0r2/s1quater/sorteo/ --out <json>
PY -B <copia>/…/s0_4/scripts/grep_convenciones.py <repo> <cada archivo de s1quater/sorteo/>
```

En los argumentos van los sha256 enteros. Acá los abrevio a 8 caracteres; enteros están en los sellos y en §1 a §5.

## 7. Repo, `.pyc`, convenciones y archivos `NO_ABRIR_`

- **Repo:** foto sha256 del repo entero (sin `.git` y sin ninguna otra exclusión), con `find` y `shasum`.
  - Antes, de 09:48:54 a 09:49:17: 50.045 archivos.
  - La de después y su comparación (`scripts/comparar_fotos_S1quater_sorteo.py`) van en el FRENO.
  - Las dos fotos enteras están en el paquete.
- **`.pyc`:** antes, 10.158 en todo el repo y 2.213 fuera de `.venv/`. El de después va en el FRENO. Todo corrió con `-B` y
  `PYTHONDONTWRITEBYTECODE=1`, desde el scratchpad y la copia.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre cada archivo de `s1quater/sorteo/`): el resultado va en el
  FRENO y en `controles/grep_convenciones_S1quater_sorteo.txt`.
- **Archivos `NO_ABRIR_`:** las cuatro salidas con ids, en el paquete, fuera del repo. Las escribieron los scripts y no las abrí: las
  leyeron solo mis scripts de control, que imprimen cuentas y sha256. Sus sha256 están en §3 a §5 y en los sellos.
- **Rutas en lo que guardo:** `<scratchpad>`, `<copia>` y `$HOME` en lugar de las rutas de la sesión.
- **Lo que no hice:** no escribí en la memoria ni en `.claude/`, no usé esperas programadas, no commiteé y no preparé ningún mensaje
  de commit.
