# U-SEG-OFICIAL — informe de S0-6b (13/10/2026)

El parche de S0-6a-bis aplicado al repo, una sola vez, con sus controles, la tabla de reprocesamiento corregida y el
control de las leídas. USD 0, sin API. **Nada commiteado y ningún mensaje de commit preparado** (el commit lo arma la
mesa). Ids de unidades: solo los de las 40 filas y las 286 leídas de S1-ter (la regla única de S1-quater, decisión 3 de
la autora); el texto de cualquier unidad y los ids de cualquier otra van a archivos `NO_ABRIR_` del paquete de revisión,
escritos por script y sin abrirlos. Las rutas `controles/…`, `censos/…`, `manifiestos/…` y `scripts/…` son de `s0_6/b/`.

## 1. Entrada

- Paso 0: `pwd` = la raíz del repo; HEAD `b487f5cb` («Segmentacion oficial: decisiones sobre la correccion ajustada, y
  una entrada nueva del backlog»); `git status --porcelain` sobre `e0_chunking/`, la tabla de reprocesamiento y `s0_6/`,
  vacío; el código de E0, el de S0-5b (`bd2190ad…`, `68bd74b5…`, `789630b5…`); `s0_6/b` no existía.
- Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md` en HEAD: `5edfd993…`, el del despacho. Las decisiones de la
  autora sobre el FRENO de S0-6a-bis (`s0_6/bis/decisiones_sobre_el_FRENO_S0-6a-bis_mesa.md`): me tocan la 4 (las anclas) y
  la 9 (el control de las leídas).
- Del paquete de la mesa leí solo el script del control de anclas por contenido (`e4de432c…`, el del despacho). No abrí
  ninguna de las carpetas que el despacho prohíbe ni ningún archivo `NO_ABRIR_`.
- Foto sha256 del repo entero, sin `.git` y sin ninguna otra exclusión (`s0_6/bis/scripts/foto_repo_entero_S0-6a-bis.py`),
  antes de escribir: 00:45:27, 50.351 archivos; `.pyc` fuera de `.venv/`, 2.213.

## 2. El parche, una sola vez (paso 1)

- `s0_6/bis/parche/parche_e0_S0-6a-bis.diff`: sha256 `a0f291c487bb243ffea1d9bbc56fb26990f7c147b3ef4ef49d4b74ded55a581f`, el
  del despacho.
- Antes de aplicarlo guardé en el scratchpad, para el control del paso 3, una copia de `e0_lib.py`, `correr_e0.py` y
  `selftest_e0.py` de S0-5b y la tabla de reprocesamiento de HEAD (`git show HEAD:…`, `6d692508…`).
- En seco, desde `e0_chunking/` (`patch -p1 --dry-run`): rc 0, los tres archivos, sin offset ni fuzz
  (`controles/parche_en_seco_S0-6b.txt`).
- Aplicado una sola vez (`patch -p1`): rc 0, sin `.orig` ni `.rej` (`controles/parche_aplicado_S0-6b.txt`). Sha256
  finales: `e0_lib.py` `d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298`, `correr_e0.py`
  `78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e`, `selftest_e0.py`
  `eb4f11e61981476957aceadb67bfbf80934c8f903c11760b41fc2530bbe38282`, los del LEEME.
- `git diff --stat`, después del parche: solo esos tres archivos (+1930 −66; `e0_lib.py` 1172, `correr_e0.py` 101,
  `selftest_e0.py` 723 renglones cambiados).
- El interruptor del prototipo no está: `S0_6_REGLAS` y `S0_6_TANDA0` dan 0 en los tres archivos.

## 3. Los controles (paso 2)

Con el código del repo, sobre una copia hecha con `rsync -a --no-links` (sin `.git`, `.venv`, `.venv-app`, `__pycache__`
ni `.DS_Store`; 22.002 archivos, 0 enlaces) después de aplicar el parche, y una raíz mínima armada de ella
(`s0_4/scripts/raiz_minima.sh`); las salidas, en el scratchpad. Intérprete: el `.venv` del repo con `-B` y
`PYTHONDONTWRITEBYTECODE=1`; los scripts de solo lectura, con `/usr/bin/python3 -B`.

| control | resultado | archivo (`controles/`) |
|---|---|---|
| los 152, dos veces (`scripts/lote_controles_S0-6b.sh`, 00:47:45-00:57:42) | 768 de 768 iguales entre sí; `por_to/` sin diferencias; **10.478 unidades** | `comparar_c152_2_vs_c152_1_S0-6b.txt`, `diff_por_to_c152_S0-6b.txt` (vacío), `lote_controles_S0-6b.log` |
| el manifiesto de la salida (`scripts/manifest_salida_S0-6b.py`, formato del de S0-6a-bis; `commit_codigo` «PENDIENTE (lo fija el commit de la autora)») contra el de S0-6a-bis (`991ac178…`) | **768 de 768 archivos `e0/` con el mismo sha256**; 10.478 unidades en los dos, iguales por TO; el mismo sha256 del código | `../manifiestos/manifest_salida_e0_152_S0-6b.json` (`80adbd58…`), `comparar_manifiesto_S0-6b_vs_S0-6a-bis.json` |
| la tanda 0, `s0_1/scripts/correr_tanda0.py`, dos veces (00:57:42-01:02:10), contra `salida_tanda0_r2b/` | **57 de 57** en las dos; 2.439 unidades | `comparar_t0_1_vs_r2b_S0-6b.txt`, `comparar_t0_2_vs_r2b_S0-6b.txt` |
| los 25 archivos de la tanda 0 dentro de los 152 (`s0_4/scripts/control_tanda0_en_152.py`) | **25 de 25**; agregados: 20 iguales y 15 ausentes en los dos | `control_tanda0_en_152_S0-6b.txt` |
| los selftests, sobre la copia (`scripts/selftests_S0-6b.sh`) | **`selftest_e0` 251 de 251**, rc 0; **b52 39 de 39, b581 34 de 34, b582 59 de 59 y b583 33 de 33**, rc 0. Sus salidas llevan el detalle de cada caso, con ids y texto de unidades: van al `NO_ABRIR_`; el resumen, en cuentas | `resumen_selftests_S0-6b.json` (`scripts/resumen_selftests_S0-6b.py`), `sha_codigo_selftests_S0-6b.txt` |
| la continuidad (`s0_5/scripts/control_continuidad_numeracion.py` sobre la corrida 1; cuentas con `s0_6/bis/scripts/continuidad_cuentas_S0-6a-bis.py`) | **70 saltos** (21 de la clase i y 49 de la ii; antes 88, 28 cierran y 10 nuevos): las cuentas, por documento y clase, iguales a las de S0-6a-bis (sin el campo de la primera corrida de S0-6a, que S0-6b no calcula); el JSON del control (`5c96d6ad…`), igual byte a byte al de después de S0-6a-bis (el sha256 que lista `s0_6/bis/FRENO_S0-6a-bis.md`) | `continuidad_cuentas_S0-6b.json`, `comparar_continuidad_S0-6b.json` (`scripts/comparar_continuidad_S0-6b.py`); el JSON del control, con rótulos e ids, en el `NO_ABRIR_` |
| las claves de la caché, después del paso 3 (`scripts/clave_cache_S0-6b.sh`: copia a la copia la tabla corregida, `29334c5d…`) | **VEREDICTO OK**; contra el de S0-6a-bis (`923dd900…`), una sola diferencia: `contraste_tabla.filas`, 44 → 45, con la fila F19d insertada en la posición 37 (después de F19b); sin ella, la lista es igual a la de S0-6a-bis. El JSON nuevo (`d1050488…`) lleva claves con ids de unidades de la tanda 0: va al `NO_ABRIR_` | `comparar_clave_cache_S0-6b.json` (`scripts/comparar_clave_cache_S0-6b.py`), `resumen_selftests_S0-6b.json` |

## 4. La tabla de reprocesamiento (paso 3; decisión 4 de la autora)

`data/experiment/mantenimiento/tabla_reprocesamiento.md`, de `6d692508…` a `29334c5d…`, con `scripts/corregir_tabla_S0-6b.py`
(cada texto viejo tiene que aparecer una sola vez en su renglón, o frena sin escribir):

- **Las 27 citas al código de E0** de `s0_6/bis/controles/anclas_e0_tabla_S0-6a-bis.txt`, con el código aplicado:
  - las 12 que quedan iguales no se tocan;
  - las 14 que se mueven pasan al rango de ese archivo: F16b `correr_e0.py:1688-1689 → :1767-1768` y
    `e0_lib.py:1391-1421 → :1602-1632`; F18a `e0_lib.py:925-979 → :1131-1185` y `:1718-1719 → :2068-2069`; F18b
    `e0_lib.py:1718-1719 → :2068-2069`; F19b `correr_e0.py:432-444 → :474-486`, `:681-690 → :723-732`, `:1393 → :1452`,
    `e0_lib.py:377 → :394` y `:642 → :782`; F20 `correr_e0.py:368-429 → :410-471` y `:448-486 → :490-528`; F21
    `e0_lib.py:3193-3268 → :4170-4245`; y la nota de F18a (§3 de la tabla), `e0_lib.py:1718-1719 → :2068-2069`, como la
    corrigió la mesa el 08/10/2026 (el mismo rango que en F18a y F18b);
  - la de F19b a las reglas de S0-5, `correr_e0.py:140-210`, que no se encuentra entera, pasa a dos: `:140-205` (las
    constantes de S0-5, de `REGLAS_S0_5` a `RAICES_POR_LISTA_S0_5`, iguales byte a byte a las de S0-5b) y `:246-252`
    (`_r5`, en su lugar nuevo: el parche cambia su docstring y tres renglones de los reemplazos de S0-6a).
- **La fila F19d,** después de F19b, como la propone `s0_6/bis/REPORTE_S0-6a-bis.md` (renglón 332), con los tres cambios
  del despacho: las anclas del despacho, en su orden; la variación del selftest, R24, como en F19b («sin variación propia:
  en la tanda 0 no ocurre»); y las celdas de las claves E1 y E3 que empiezan con «cambia», como en F19b.
- **Una nota fechada al pie** (el último renglón de §6, desde el renglón 520), como las del 08/10/2026 y del 10/10/2026,
  que no se editan: qué anclas cambian, de dónde a dónde, y por qué.
- **El control por contenido** (`scripts/control_anclas_contenido_S0-6b_mesa.py`, el de la mesa, `e4de432c…`, copiado sin
  cambios; `controles/control_anclas_contenido_S0-6b.txt`), con la tabla de HEAD y el código de S0-5b guardados antes del
  paso 1, la tabla corregida hasta el renglón 519 (el anterior a la nota nueva), el código aplicado y el `.diff`: **53 de
  53 controles ok**. Corrió con el `python` del `.venv` del repo (3.10), con `-I -B`: el del sistema (3.9) no admite las
  anotaciones `int | None` del script.

## 5. Las 286 leídas (paso 4; §4 del mandato y decisión 9 de la autora)

- `s0_6/scripts/control_leidas_S0-6a.py`, sin cambios, sobre la salida de los 152 (la corrida 1 de los controles) contra la
  E0 de S1-ter, como en S0-6a-bis. **Cómo lo corrí:** sin `--regla` (no las pide; el campo de las reglas solas queda
  vacío) y con `--tsv` apuntando a un TSV de solo encabezado (`controles/tsv_solo_encabezado_S0-6b.tsv`): el TSV de las
  filas está en el paquete de la mesa, del que no puedo leer nada más que el script de anclas. El TSV no cambia el corte ni
  la herencia de cada leída: solo dice si un cambio va al FRENO o tiene fila (el campo `al_freno` del `NO_ABRIR_`, que el
  archivo abierto no copia).
- **La salida con texto,** en el paquete: `NO_ABRIR_control_leidas_S0-6b.json` (`16021106…`) y `.md` (`e01c7065…`), sin
  abrirlos.
- **El archivo abierto,** `censos/control_leidas_S0-6b.json`, escrito por `scripts/control_leidas_cuentas_S0-6b.py` desde el
  JSON `NO_ABRIR_`: por leída, su id y si el corte y la herencia siguen iguales; y las cuentas: **286 leídas, 212 iguales,
  corte igual 261, herencia igual 216, cambiadas 74**.
- **El control:** el resultado de cada leída (corte igual, herencia igual o cambiada, contra S1-ter) es el mismo que en
  `s0_6/bis/censos/control_leidas_S0-6a-bis.json`: **0 leídas con otro resultado**, el mismo conjunto de 286, y las cuentas
  del JSON iguales a las calculadas.

## 6. Comandos

Sobre copias, nunca sobre el repo (salvo el parche y la tabla, que son las escrituras del despacho). `c152_1`, `c152_2`,
`t0_1` y `t0_2` son las salidas del lote de controles; `<S0-5b>`, la copia del código de S0-5b guardada antes del parche;
`<tabla de HEAD>`, la de `git show HEAD:data/experiment/mantenimiento/tabla_reprocesamiento.md`.

```
shasum -a 256 s0_6/bis/parche/parche_e0_S0-6a-bis.diff
cd data/experiment/reextraccion_v2/e0_chunking && patch -p1 --dry-run < <parche> && patch -p1 < <parche>
rsync -a --no-links --exclude /.git --exclude /.venv --exclude /.venv-app --exclude .DS_Store --exclude __pycache__ <repo>/ <copia>/
s0_4/scripts/raiz_minima.sh <copia> <raíz> <copia>/data/experiment/reextraccion_v2/e0_chunking
scripts/lote_controles_S0-6b.sh <trabajo> <copia> <raíz> <python del .venv>
scripts/selftests_S0-6b.sh <logs> <copia> <python del .venv> <tmp>
python -B ../scripts/comparar_archivos_S0-6a.py c152_2 c152_1
python -B scripts/manifest_salida_S0-6b.py --e0 c152_1 --codigo <e0_chunking del repo> --tiempos … --tiempos2 … --out manifiestos/manifest_salida_e0_152_S0-6b.json
python -B scripts/comparar_manifiestos_S0-6b.py --a s0_6/bis/manifiestos/manifest_salida_e0_152_S0-6a-bis.json --b manifiestos/manifest_salida_e0_152_S0-6b.json --out controles/comparar_manifiesto_S0-6b_vs_S0-6a-bis.json
python -B ../scripts/comparar_archivos_S0-6a.py t0_1 reextraccion_v2/e0_chunking/salida_tanda0_r2b
python -B s0_4/scripts/control_tanda0_en_152.py c152_1 reextraccion_v2/e0_chunking/salida_tanda0_r2b
python -B s0_5/scripts/control_continuidad_numeracion.py --e0 c152_1 --lineas <caché de renglones> --out <NO_ABRIR_control_continuidad>
python -B s0_6/bis/scripts/continuidad_cuentas_S0-6a-bis.py --antes s0_5/b/controles/control_continuidad_S0-5b.json --despues <NO_ABRIR_control_continuidad> --out controles/continuidad_cuentas_S0-6b.json
python -B scripts/comparar_continuidad_S0-6b.py --a s0_6/bis/controles/continuidad_cuentas_S0-6a-bis.json --b controles/continuidad_cuentas_S0-6b.json --out controles/comparar_continuidad_S0-6b.json
python -B scripts/corregir_tabla_S0-6b.py --tabla <tabla de HEAD> --out <tabla corregida>
python -I -B scripts/control_anclas_contenido_S0-6b_mesa.py --tabla-vieja <tabla de HEAD> --tabla-nueva <tabla corregida> --hasta-nueva 519 --codigo-viejo <S0-5b> --codigo-nuevo <e0_chunking del repo> --parche <parche>
scripts/clave_cache_S0-6b.sh <salida> <copia> <repo> <python del .venv> <tmp>
python -B scripts/comparar_clave_cache_S0-6b.py --antes s0_6/bis/controles/selftest_clave_cache_S0-6a-bis.json --despues <NO_ABRIR_selftest_clave_cache> --out controles/comparar_clave_cache_S0-6b.json
python -B ../scripts/control_leidas_S0-6a.py --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --base s1ter/e0 --final c152_1 --tsv controles/tsv_solo_encabezado_S0-6b.tsv --out <NO_ABRIR_….json> --md <NO_ABRIR_….md>
python -B scripts/control_leidas_cuentas_S0-6b.py --json <NO_ABRIR_….json> --referencia s0_6/bis/censos/control_leidas_S0-6a-bis.json --out censos/control_leidas_S0-6b.json
python -B scripts/resumen_selftests_S0-6b.py --salida selftest_e0=… --salida b5x=… --salida claves_cache=… --out controles/resumen_selftests_S0-6b.json
python -B s0_6/bis/scripts/foto_repo_entero_S0-6a-bis.py <repo> <foto>; python -B s0_6/bis/scripts/foto_repo_entero_S0-6a-bis.py --comparar <antes> <después>
python -B s0_4/scripts/grep_convenciones.py <repo> <archivos de s0_6/b>
```

Las rutas `s0_4/…`, `s0_5/…` y `s0_6/…` son de `segmentacion_oficial_e0r2/`; `../scripts/` es `s0_6/scripts/` (los de
S0-6a, sin cambios). `control_anclas_contenido_S0-6b_mesa.py` corre con el `python` del `.venv` (3.10).

## 7. Repo, `.pyc`, convenciones y archivos `NO_ABRIR_`

- **Repo** (`s0_6/bis/scripts/foto_repo_entero_S0-6a-bis.py`, el repo entero sin `.git` y sin ninguna otra exclusión):
  antes, a las 00:45:27, 50.351 archivos. Después de escribir, solo cambian los tres archivos de E0, la tabla de
  reprocesamiento y `s0_6/b/` (archivos nuevos); la foto de después y su comparación, en el mensaje del FRENO (este
  archivo entra en la foto).
- **`.pyc`** fuera de `.venv/`: 2.213 antes; el de después, en el mensaje del FRENO. Todo corrió con `-B` y
  `PYTHONDONTWRITEBYTECODE=1`, sobre copias.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre todos los archivos de `s0_6/b/`,
  `controles/grep_convenciones_S0-6b.txt`).
- **Ids de unidades en `s0_6/b/`:** solo los de las 286 leídas (en `censos/control_leidas_S0-6b.json`); lo controla un
  script contra la lista de las 286 y las 40 filas (`controles/ids_en_s0_6b_S0-6b.json`).
- **Archivos `NO_ABRIR_`** (en el paquete, fuera del repo; escritos por script, sin abrirlos): la salida del control de las
  leídas (JSON, md y su salida estándar), el JSON del control de continuidad, las salidas de `selftest_e0`, de los b5x y
  del selftest de claves de la caché (texto y JSON), y la salida de E0 de los 152 (corrida 1). Sus sha256, en el FRENO.
- Los logs y salidas que guardo llevan `<scratchpad>` y `<home>` en lugar de las rutas de la sesión. No escribí en la
  memoria ni en `.claude/`, y no usé esperas programadas.
