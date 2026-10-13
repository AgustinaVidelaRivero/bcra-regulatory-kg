# U-SEG-OFICIAL — FRENO S0-6b (13/10/2026)

El parche de S0-6a-bis aplicado al repo, una sola vez, con sus controles. Ids de unidades: solo los de las 40 filas y
las 286 leídas de S1-ter; el texto de cualquier unidad y los ids de cualquier otra van a archivos `NO_ABRIR_` del paquete,
escritos por script y sin abrirlos.

Paso 0 (la ruta, con `$HOME` en lugar del directorio de la usuaria):

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --oneline -1
b487f5cb Segmentacion oficial: decisiones sobre la correccion ajustada, y una entrada nueva del backlog
$ git status --porcelain -- data/experiment/reextraccion_v2/e0_chunking data/experiment/mantenimiento/tabla_reprocesamiento.md data/experiment/segmentacion_oficial_e0r2/s0_6
$ shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
bd2190ad50515ee900448c25dc8e663b3b7d7c52b9e4d8e874f7442b3bec7a51  data/experiment/reextraccion_v2/e0_chunking/e0_lib.py
68bd74b501af7023e97ac837d40390e0732e167dba1f0a5c73f39fc859c2787d  data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
789630b5c0995075392b6590730d5105c39765c611ad840914f606b67b9ce3c0  data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
$ ls data/experiment/segmentacion_oficial_e0r2/s0_6/b
ls: data/experiment/segmentacion_oficial_e0r2/s0_6/b: No such file or directory
```

Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md` en HEAD: `5edfd993…` (el del despacho). Del paquete de la
mesa leí solo `control_anclas_contenido_S0-6b_mesa.py` (`e4de432c…`, el del despacho). USD 0, sin API. **Nada commiteado,
ningún mensaje de commit preparado; no escribí en la memoria.** Escribí los tres archivos de E0 (por el parche), la tabla
de reprocesamiento y `s0_6/b/`. Detalle: `REPORTE_S0-6b.md`.

**El parche** (paso 1; REPORTE, §2): `s0_6/bis/parche/parche_e0_S0-6a-bis.diff`, `a0f291c4…` (el del despacho). Antes,
guardé en el scratchpad el código de S0-5b y la tabla de HEAD (`6d692508…`). En seco, rc 0, los tres archivos, sin offset
ni fuzz; aplicado una sola vez, rc 0, sin `.orig` ni `.rej`; sha256 finales `e0_lib.py` `d89aab1a…`, `correr_e0.py`
`78c54c4c…`, `selftest_e0.py` `eb4f11e6…` (los del LEEME); `git diff --stat`, solo esos tres; `S0_6_REGLAS` y
`S0_6_TANDA0`, 0 en los tres.

**Los controles** (paso 2; REPORTE, §3), con el código del repo, sobre una copia hecha con `rsync`, sin enlaces:
- **los 152, dos veces:** 768 de 768 iguales entre sí, **10.478 unidades**; el manifiesto
  `manifiestos/manifest_salida_e0_152_S0-6b.json` (`80adbd58…`, `commit_codigo` «PENDIENTE (lo fija el commit de la
  autora)»): sus 768 archivos `e0/` dan **los mismos sha256 que el de S0-6a-bis** (`991ac178…`);
- **la tanda 0:** 57 de 57, dos veces (2.439 unidades); los 25 de la tanda 0 dentro de los 152, **25 de 25**;
- **los selftests:** `selftest_e0` **251 de 251**; b52 39 de 39, b581 34 de 34, b582 59 de 59, b583 33 de 33;
- **la continuidad:** **70 saltos**, con las cuentas por documento y clase iguales a las de S0-6a-bis; el JSON del control
  (`5c96d6ad…`) es igual byte a byte al de después de S0-6a-bis (el sha256 que lista `s0_6/bis/FRENO_S0-6a-bis.md`);
- **las claves de la caché**, después del paso 3: **VEREDICTO OK**; contra el de S0-6a-bis (`923dd900…`), la única
  diferencia es `contraste_tabla.filas` 44 → 45: la fila F19d, insertada después de F19b; sin ella, igual
  (`controles/comparar_clave_cache_S0-6b.json`).

**Las anclas** (paso 3; decisión 4; REPORTE, §4), en `data/experiment/mantenimiento/tabla_reprocesamiento.md`
(`6d692508…` → `29334c5d…`):
- las 12 citas que quedan iguales, sin tocar;
- las 14 que se mueven: F16b `correr_e0.py:1688-1689 → :1767-1768` y `e0_lib.py:1391-1421 → :1602-1632`; F18a
  `e0_lib.py:925-979 → :1131-1185` y `:1718-1719 → :2068-2069`; F18b `e0_lib.py:1718-1719 → :2068-2069`; F19b
  `correr_e0.py:432-444 → :474-486`, `:681-690 → :723-732`, `:1393 → :1452`, `e0_lib.py:377 → :394` y `:642 → :782`; F20
  `correr_e0.py:368-429 → :410-471` y `:448-486 → :490-528`; F21 `e0_lib.py:3193-3268 → :4170-4245`; la nota de F18a,
  `e0_lib.py:1718-1719 → :2068-2069`;
- F19b `correr_e0.py:140-210` (no se encuentra entera) pasa a `:140-205` (las constantes de S0-5) y `:246-252` (`_r5`);
- la fila F19d, después de F19b, con las anclas del despacho, R24 en la variación y «cambia» en E1 y E3;
- una nota fechada al pie (13/10/2026); las anteriores no se editan.

Control por contenido (`scripts/control_anclas_contenido_S0-6b_mesa.py`, el de la mesa, sin cambios;
`controles/control_anclas_contenido_S0-6b.txt`): **53 de 53 controles ok**. Corrió con el `python` del `.venv` (3.10): el
del sistema (3.9) no admite las anotaciones `int | None` del script.

**El control de las 286 leídas** (paso 4; decisión 9; REPORTE, §5): `s0_6/scripts/control_leidas_S0-6a.py` sobre la
corrida 1 de los 152 contra la E0 de S1-ter, **sin `--regla` y con un TSV de solo encabezado**: el TSV de las filas está en
el paquete de la mesa, del que solo puedo leer el script de anclas; el TSV no cambia el corte ni la herencia de cada
leída, solo el campo `al_freno`, que el archivo abierto no copia. Su salida con texto, en el `NO_ABRIR_` (JSON
`16021106…`). En `censos/control_leidas_S0-6b.json`, solo ids de las leídas y cuentas: **286 leídas, 212 iguales, corte
igual 261, herencia igual 216, cambiadas 74**; el resultado de cada leída, **el mismo que en S0-6a-bis** (0 distintas).

**Repo, `.pyc` y convenciones** (REPORTE, §7): foto sha256 del repo entero (sin `.git`) antes, 00:45:27, 50.351 archivos;
`.pyc` fuera de `.venv/`, 2.213 antes; grep de convenciones sobre `s0_6/b/` en `controles/grep_convenciones_S0-6b.txt`;
en `s0_6/b/`, solo ids de leídas (286, en `censos/control_leidas_S0-6b.json`; `controles/ids_en_s0_6b_S0-6b.json`). La foto y
los `.pyc` de después, en el mensaje del FRENO (este archivo entra en la foto).

**Archivos `NO_ABRIR_`** (en el paquete, fuera del repo; escritos por script, sin abrirlos):
- `NO_ABRIR_control_continuidad_S0-6b.json` `5c96d6ad9c361b8f9c96275c5cf8befd91fc609d5a5c59540e84717138b95f4c`
- `NO_ABRIR_control_leidas_S0-6b.json` `16021106a0ef00b151459c2a4c64c065612159ce066be0b54dd0d465c55f0002`
- `NO_ABRIR_control_leidas_S0-6b.md` `e01c70655d2cc58d91cfc1fe795ee5767ce35d16b499a5f6f9935998e090e30d`
- `NO_ABRIR_control_leidas_salida_S0-6b.txt` `8181cf18076847aea86134e5c7fc8273a4d6f3d3e15dc6f1350436130b0791c0`
- `NO_ABRIR_e0_152_S0-6b.tar.gz` `2e088e6873115fb349f2e35d1e12ee9341289023002b2dcde20da170370de8ba`
- `NO_ABRIR_selftest_clave_cache_S0-6b.json` `d10504888becd89439218b0794462178b4bc54a89483428fef3485b97ab3f4b0`
- `NO_ABRIR_selftest_claves_cache_S0-6b.txt` `fd78eb883d3bb0e2b74a939c103a69c3b1a8b1edae3f8f69af1d14088549b465`
- `NO_ABRIR_selftest_e0_S0-6b.txt` `dff7fe7e3f57a16c27b712de9c9780ad4356aa26216d1c9d2a349ad3ae94464c`
- `NO_ABRIR_selftests_b5x_S0-6b.txt` `4ebb86266c6f473aa8708a9433ad72d6bf6a5c151b73e090448544f091046778`

**Cierre:** el paquete `revision_USEG_OFICIAL_FRENO_S0-6b/`, con su `manifest.txt`, copiado con `ditto` a
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/3affae38-5acf-4382-b2ca-6d7f152ddb34/scratchpad/revision_USEG_OFICIAL_FRENO_S0-6b/`;
la verificación de esa copia contra el `manifest.txt` va en el mensaje del FRENO. Nada commiteado, ningún mensaje de
commit preparado (el commit lo arma la mesa), nada escrito en la memoria.

FRENO.
