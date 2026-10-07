# U-RERESOL-CAT — FRENO R2-1 bis: W1 a W3 aplicados al repo (06/10/2026)

Despacho del 06/10/2026, tras la revisión del FRENO R2-1. USD 0; sin API ni Neo4j. HEAD `9502ca4`; nada commiteado.

**Precondiciones.** `git log --oneline -1 -- data/experiment/sincola_t0` da `dde9f44`; `git status --short` de la fixture, `grafos.py` y
`sincola_t0` sale vacío; `git diff --stat 26c6502 HEAD` sobre los tres archivos sale vacío (son la base de los parches); `git apply --check`
de los tres parches del paquete de R2-1 da limpio.

**Parches aplicados** con `git apply`; `git diff --numstat`: `ensamblar_tanda0.py` 39/11, `r1_e4.py` 70/3, `regression_kg.py` 29/7. Los tres
quedan byte a byte iguales al código verificado en R2-1 (`70508d54…`, `98ac0d71…`, `ee120c78…`). En el repo no escribí nada más que este freno.

**Controles** sobre una copia nueva del árbol de trabajo con los parches (`rsync --no-links`: 0 enlaces, 0 `.pyc`), con `controles_r2_1.sh`:
- **Suite**, seis entradas selladas: con el código de HEAD puesto en la copia y con el del repo, `.json` y `.md` byte a byte iguales en las
  seis. Diferencia con el despacho (regla d): contra la salida de HEAD guardada en R2-1 difieren la ruta de la copia, el sha de la fixture
  (cambiada por SC2 en `dde9f44`) y la regresión de las dos entradas sin cola, que ahora tienen entrada en la fixture; ningún estado de ítem
  cambia. Por eso la base byte a byte es la de HEAD corrida en la misma copia.
- **Cadenas**, sin parámetro: r2a `70d51e42…` y `fa4c1043…`; r2b `a9631a64…` y `6e756043…`; sin cola con `--sin-cola`, `e22fae1a…` y
  `2922b72d…`. En los cuatro r2b, `r2/` es igual a lo sellado salvo el reporte (33 y 23 archivos).
- **Catálogo sin ampliaciones** con `--catalogo-resolucion` (generados iguales a `generados_r2/`): r2b diez `a9631a64…` y, con `--sin-cola`,
  `e22fae1a…`; 33 archivos iguales en cada uno.
- **Selftests** con el código del repo: `selftest_reresolver_catalogo` 51/51, `selftest_r3` 116/116, `selftest_regression_kg` 184/184,
  `selftest_catalogo_unico` 60/60 (con `GIT_DIR` apuntando al `.git` del repo, solo lectura).

**Cierre.** sha256 de todos los archivos del repo (salvo `.git` y `.venv`), antes de aplicar (22.935) y después, antes de este freno (22.941):
cambian 3, los de W1 a W3; aparecen 6, en `data/experiment/lectura_aceptadas/` (otra sesión, U-LECTURA-ACEPTADAS); desaparecen 0. En las
carpetas que lee la unidad (1.200 archivos: ensamblador, `corpus_v2`, `e2_reduce`, `pyd_r2/code`, `scripts`, catálogo, E0 r2a y r2b,
`corpus_tanda0`, manifiestos, `reresolucion_catalogo`, `r2_codigo`) cambian solo esos tres; los ensamblados sellados están intactos. `.pyc`
fuera de `.venv`: 2.213. El grep de convenciones (términos del §9 del FRENO R2-1) sobre este freno y el paquete sale vacío. Sin tocar: la
parte B, el estado de las filas por calificador, `validador_r2.py`, el catálogo y la fixture. Paquete `revision_URERESOL_CAT_FRENO_R2-1bis/`.
**Commit PENDIENTE de la autora** (W1 a W3 junto con lo de R2-1). FRENO.
