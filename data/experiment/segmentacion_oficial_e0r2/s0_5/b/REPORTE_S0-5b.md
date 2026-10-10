# U-SEG-OFICIAL — Informe de S0-5b (10/10/2026)

S0-5b aplica al repo, una sola vez, el código de E0 de S0-5a-bis y corre sus controles. Hay una sola fuente de
alcance: el mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, con sus notas al pie hasta la del
10/10/2026, leída en `3c5f0034`, y el «seguí» de S0-5b. USD 0, sin API.
**Nada commiteado** y ningún mensaje de commit preparado: el commit lo arma la mesa. S0-5b no agrega reglas.

## 1. Entrada (`controles/precondiciones_S0-5b.txt`)

- **Commits en el log:**
  - `97a54a5c` (registro de S0-5a-bis, 43 archivos en `s0_5/bis/`);
  - `3c5f0034` (notas de la mesa del 10/10/2026), que es HEAD.
- **La nota del 10/10/2026 del mandato**, leída en `3c5f0034` (`a6c7de69…`, igual al archivo de ese momento). Dice:
  - que el interruptor no se aplica;
  - que el `selftest_e0.py` de la corrida FINAL de la segunda vuelta era `9921eae1…`, sin efecto sobre la salida;
  - el detalle 104 → 88 de la continuidad;
  - que snp_cheq 3.3.6.1 queda aceptado;
  - que la corrección de 23 a 22 es de la mesa.
- **E0 del repo antes del parche, el de S0-4b:** `e0_lib.py` `65a8c3b8…`, `correr_e0.py` `94d35349…` y `selftest_e0.py`
  `ec186071…`, iguales a HEAD.
- **El parche en el repo:** `s0_5/bis/parche/parche_e0_S0-5a-bis.diff` da `421ee913…`, igual que en `97a54a5c`.
- **Foto sha256 del repo** (`s0_1/scripts/snapshot_repo.py`): a las 00:53:39, 48.589 archivos.
- **`.pyc`** fuera de `.git/` y `.venv/`: 2.213.

## 2. El parche, una sola vez (`controles/parche_aplicado_S0-5b.txt`)

Desde `data/experiment/reextraccion_v2/e0_chunking/`:

- **Prueba en seco:** `patch -p1 --dry-run < …/parche_e0_S0-5a-bis.diff` da rc 0, con los tres archivos y sin offset
  ni fuzz.
- **Aplicación:** `patch -p1 < …/parche_e0_S0-5a-bis.diff` a las 00:54:01, rc 0, sin `.orig` ni `.rej`.
- **sha256 después:** `e0_lib.py` `bd2190ad50515ee9…`, `correr_e0.py` `68bd74b501af7023…` y `selftest_e0.py`
  `789630b5c0995075…`. Son los tres esperados e iguales byte a byte a los finales de S0-5a-bis.
- **`git diff --stat`, recién aplicado:** solo esos tres archivos, +1.167 −23.
- **El interruptor del prototipo** (`interruptor_prototipo_S0-5a-bis.diff`) no se aplicó: `S0_5_REGLAS` y
  `S0_5_TANDA0` no aparecen en los tres archivos (`grep -c`, 0 en cada uno).

## 3. Controles, con el código del repo y las salidas en una copia (CLAUDE.md §4.l)

**Copia** (`controles/copia_contra_repo_S0-5b.txt`):
- `rsync -a --no-links` del repo ya aplicado al scratchpad, sin `.git/`, `.venv/`, `.venv-app/`, `__pycache__/` ni
  `.DS_Store`; 0 enlaces.
- En los directorios que leen los controles, la copia es igual al repo (`diff -rq`). La única diferencia es un archivo
  de `s0_5/bis/censos/` que otra mano escribió en el repo después de la copia (§6), y ningún control lo lee.
- Los 152 y la tanda 0 corrieron desde una raíz mínima armada de la copia (`s0_4/scripts/raiz_minima.sh`), sin enlaces.
- El código fue el mismo en los tres lugares: el repo, la copia y la raíz (`controles/sha_codigo_controles_S0-5b.txt`).
- Intérprete: el `.venv` del repo con `-B` y `PYTHONDONTWRITEBYTECODE=1`; los scripts de solo lectura, con
  `/usr/bin/python3 -B`.
- Lote: `scripts/lote_controles_S0-5b.sh` y `scripts/selftests_S0-5b.sh`.

| control | resultado | archivo (`controles/`) |
|---|---|---|
| los 152, corrida 1 (00:56:13–01:01:24, 152 TOs, 0 con error) contra el manifiesto de S0-5a-bis `176cbdc0…` | 768 de 768 iguales; **9.665 unidades** | `comparar_c152_1_vs_manifiesto_S0-5a-bis_S0-5b.txt` |
| corrida 1 contra la salida final de la segunda vuelta de S0-5a-bis (archivos) | 768 de 768 iguales | `comparar_c152_1_vs_c_FINAL_S0-5a-bis_S0-5b.txt` |
| los 152, corrida 2 (01:01:24–01:06:16), contra la corrida 1 | 768 de 768 iguales; `por_to/` sin diferencias | `comparar_c152_2_vs_c152_1_S0-5b.txt` |
| corrida 2 contra el manifiesto `176cbdc0…` | 768 de 768 iguales | `comparar_c152_2_vs_manifiesto_S0-5a-bis_S0-5b.txt` |
| manifiesto de la corrida 1 contra `176cbdc0…`, campo por campo | código, archivos, TOs, unidades, unidades por TO y sha256 iguales; solo cambia el texto de `unidad` | `../manifiestos/manifiesto_salida_e0_152_S0-5b.json` |
| tanda 0 (01:06:16–01:08:31, `s0_1/scripts/correr_tanda0.py`) contra `salida_tanda0_r2b/` | **57 de 57** iguales; 2.439 unidades | `comparar_t0_vs_r2b_S0-5b.txt` |
| los 25 archivos de la tanda 0 dentro de los 152 | 25 de 25; agregados: 20 iguales y 15 ausentes en los dos | `control_tanda0_en_152_S0-5b.txt` |
| `selftest_e0` | **188/188**, rc 0; mismo texto que en S0-5a-bis, salvo el directorio temporal | `selftest_e0_S0-5b.txt` |
| b52, b581, b582, b583 | 39/39, 34/34, 59/59, 33/33, rc 0 | `selftests_b5x_S0-5b.txt` |
| selftest de claves de la caché | **VEREDICTO OK**; anclaje r2b OK (2.449 claves); contraste con la tabla OK; salida igual byte a byte al JSON del repo, `923dd900…` | `selftest_claves_cache_S0-5b.txt`, `selftest_clave_cache_S0-5b.json` |
| control de continuidad sobre la corrida 1 | **88 saltos**; JSON y lista iguales byte a byte a los de S0-5a-bis (§4) | `control_continuidad_S0-5b.json`, `lista_continuidad_S0-5b.md` |
| selftest del control de continuidad (S0-4b contra la corrida 1) | 14/14; mismo texto que en S0-5a-bis | `selftest_control_continuidad_S0-5b.txt` |

**Bases de las comparaciones:**
- La base S0-4b del selftest de continuidad es la salida «todas apagadas» de S0-5a-bis. Controlé otra vez que es igual
  al manifiesto de S0-4b (`61ed4bc9…`, el de su paquete): 768 de 768, 9.625 unidades
  (`comparar_base_S0-4b_vs_manifiesto_S0-5b.txt`).
- El «antes» de la lista de continuidad es `s0_5/censos/control_continuidad_antes_S0-5a.json`, que está commiteado.
- La caché de renglones es la de S1-bis (152 archivos), la misma de S0-5a-bis.

**La diferencia sin efecto que anota la mesa** (`selftest_e0.py` `9921eae1…` en la corrida FINAL de la segunda vuelta)
no se repite acá. Las dos corridas de los 152, la tanda 0 y los selftests corrieron con `789630b5…`, y la salida es la
del manifiesto `176cbdc0…` byte a byte. Eso confirma que el docstring de `selftest_e0.py` no toca la salida de E0.

**Manifiestos** (`manifiestos/`):
- `manifiesto_salida_e0_152_S0-5b.json`: el sha256 y los bytes de los 768 archivos, y las unidades por TO;
- `manifiesto_salida_e0_tanda0_S0-5b.json`: los 57 archivos, 10 TOs y 2.439 unidades.

Los dos salen de `s0_5/scripts/manifiesto_salida_S0-5a.py`. La salida misma va en el paquete
(`e0_salida_S0-5b.tar.gz`: `c152_1/` y `t0/`).

## 4. Continuidad, 104 → 88, caso por caso (`controles/lista_continuidad_S0-5b.md`)

La lista es igual byte a byte a `s0_5/bis/censos/lista_continuidad_S0-5a-bis.md`: 17 se cierran, 1 es nuevo y 1 sigue
cambiando de unidad.

**Se cierran 11 por R5-f**, todos de ri_ccna y todos huecos (ii) sin descendientes tragados:
- D1A1: 2.1.1 a 2.1.8, antes en `ri_ccna::D1A1::2.1::intro`;
- D1A1: 5.1 y 8.1, antes en `ri_ccna::D1A1::S5::chapeau_seccion` y `::S8::chapeau_seccion`;
- D1A2: 5.1, antes en `ri_ccna::D1A2::S5::chapeau_seccion`.

**Se cierran 6 por R5-d**:
- `ri_rml` 1.2.4 (ii, cola), antes en `ri_rml::1.3`;
- `snp_tr` 1.3.4, 1.3.5 y 1.3.6 (ii, cola) y 1.4 y 1.5 (ii, hueco), antes en `snp_tr::1.6::intro`, con 2, 3, 2, 4 y 4
  descendientes tragados (15).

**Aparece 1:** snp_cheq 3.3.6.1, de clase (i) y hueco. Es el salto del PDF aceptado por la nota del 10/10/2026.
3.3.6 sigue como (i), de forma «padre», sin descendientes tragados.

**La cuenta:** 104 − 11 − 6 + 1 = 88.
- Por clase: 16 (i) y 72 (ii); 1 (ii) con posible referencia.
- 12 documentos con saltos.
- Tanda 1: 5 saltos, todos (i), en 3 documentos.
- Para la autora, 72: 71 fuera de la tanda 1 y 1 de la tanda 0 (`ctacte` 1.3.1.9).

## 5. Lo que encontré: límites medidos, caso por caso

1. **Las anclas de la tabla de reprocesamiento al código de E0**
   (`data/experiment/mantenimiento/tabla_reprocesamiento.md`; `controles/anclas_e0_tabla_S0-5b.txt`, con
   `scripts/anclas_e0_tabla_S0-5b.py`).
   - Método: tomé los renglones citados en el código de S0-4b y los busqué, enteros, en el código aplicado.
   - De 17 citas a `e0_lib.py` o `correr_e0.py`, **3 quedan donde estaban**: F01 `correr_e0.py:86-94`, F19b
     `correr_e0.py:95-100` y F21 `correr_e0.py:77-80`.
   - **Las otras 14 se mueven**, con el bloque entero en otro rango:

     | fila | antes | después |
     |---|---|---|
     | F16b | `correr_e0.py:1582-1583` | `:1688-1689` |
     | F16b | `e0_lib.py:1305-1335` | `:1391-1421` |
     | F18a | `e0_lib.py:839-893` | `:925-979` |
     | F18a, F18b y la nota de F18a (renglón 284) | `e0_lib.py:1590-1591` | `:1718-1719` |
     | F19b | `correr_e0.py:360-372` | `:432-444` |
     | F19b | `correr_e0.py:609-618` | `:681-690` |
     | F19b | `correr_e0.py:1302` | `:1393` |
     | F19b | `e0_lib.py:360` | `:377` |
     | F19b | `e0_lib.py:556` | `:642` |
     | F20 | `correr_e0.py:296-357` | `:368-429` |
     | F20 | `correr_e0.py:376-414` | `:448-486` |
     | F21 | `e0_lib.py:2718-2793` | `:3193-3268` |

     Las 14 son: 2 de F16b, 2 de F18a, 1 de F18b, 5 de F19b, 2 de F20, 1 de F21 y 1 de la nota.
   - El bloque de `:1590-1591` aparece dos veces, antes y después; la cita es la primera aparición en los dos.
   - Ninguna cita queda sin encontrar.
   - **No toqué la tabla:** S0-5b solo autoriza escribir en los tres archivos de E0, `s0_5/b/` y el scratchpad. En
     S0-4b la tabla entró al commit con F19b.
   - El contraste del selftest de claves con la tabla da OK, porque no lee los renglones citados.
   - **Para la mesa, dos cosas:**
     - corregir las 14 citas;
     - decidir si F19b, que cita las reglas de S0-2, cita también las de S0-5 (R5-a a R5-g). La descripción de la
       fila («una unidad agregada o retirada por una regla de segmentación de E0») ya las cubre.
2. **Ningún límite nuevo en la salida.** La salida de E0 del repo es la de S0-5a-bis, byte a byte. Las listas de límites
   de S0-5a-bis se derivan de esa salida, así que siguen valiendo sin cambios: los 209 de
   `s0_5/bis/censos/limites_S0-5a-bis.md` y los 88 saltos. No las regeneré.

## 6. Repo, `.pyc` y convenciones

- **Foto sha256 del repo** (`s0_1/scripts/snapshot_repo.py`, con sus exclusiones; `controles/comparacion_fotos_S0-5b.txt`).
  A las 00:53:39 había 48.589 archivos y a las 01:20:31, 48.619; HEAD `3c5f0034` las dos veces. Hay 30 nuevos, 0
  borrados y 6 cambiados.
  - **De S0-5b:** los 3 archivos de E0 (cambiados, por el parche) y los 29 nuevos de `s0_5/b/`. Ningún otro.
  - **De otra mano (4).** No los escribí: en esta sesión solo los leí. Ninguno estaba commiteado al cerrar.
    - `s0_5/bis/censos/manifiesto_salida_e0_152_S0-5a-bis_nota_10-10-2026.md`: sin rastrear, 00:57:59. Es la nota de
      la mesa sobre el `selftest_e0.py` de la corrida FINAL, que el §3 confirma.
    - Tres mandatos de `docs/mandatos/` en el árbol de trabajo, con notas nuevas al pie y solo agregadas al final
      (`git diff --numstat`: +14, +21 y +25; 0 renglones quitados): `USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`
      (00:59:32), `UCONF_MATRIZ_lectura_confirmacion.md` (01:00:04) y `UOMISIONES_COD_release_codigo_ensamblado.md`
      (01:07:00).
    - La nota nueva del mandato de S0-5a no es fuente de S0-5b: no está commiteada y es posterior al «seguí».
- **`.pyc`** (sin `.git/` ni `.venv/`): 2.213 antes y después, la misma lista.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py` sobre `s0_5/b/` y sus subdirectorios;
  `controles/grep_convenciones_S0-5b.txt`): control positivo 16 de 16; 29 archivos; **0 coincidencias** (ningún nombre de persona, ninguna referencia al origen de una decisión, ninguna ruta absoluta; los logs de los selftests llevan `<scratchpad>` en lugar de la ruta).

## 7. Comandos

Sobre la copia (`<copia>`) y el directorio de trabajo (`<w>`); `<py>` es el `.venv` del repo.

```
# parche, desde data/experiment/reextraccion_v2/e0_chunking/
patch -p1 --dry-run < ../../segmentacion_oficial_e0r2/s0_5/bis/parche/parche_e0_S0-5a-bis.diff
patch -p1 < ../../segmentacion_oficial_e0r2/s0_5/bis/parche/parche_e0_S0-5a-bis.diff
# copia y raíz mínima
rsync -a --no-links --exclude /.git --exclude /.venv --exclude /.venv-app --exclude .DS_Store --exclude __pycache__ <repo>/ <copia>/
s0_4/scripts/raiz_minima.sh <copia> <w>/raices/repo <copia>/data/experiment/reextraccion_v2/e0_chunking
# los 152 dos veces y la tanda 0; selftests
s0_5/b/scripts/lote_controles_S0-5b.sh <w> <copia> <py>
s0_5/b/scripts/selftests_S0-5b.sh <w> <copia> <py>
# comparaciones y manifiestos
python -B s0_5/scripts/comparar_salidas_S0-5a.py <w>/corridas/c152_k --manifiesto s0_5/bis/censos/manifiesto_salida_e0_152_S0-5a-bis.json
python -B s0_5/scripts/comparar_salidas_S0-5a.py <w>/corridas/c152_2 --otra <w>/corridas/c152_1
python -B s0_5/scripts/comparar_salidas_S0-5a.py <w>/corridas/t0 --otra <repo>/…/e0_chunking/salida_tanda0_r2b
python -B s0_4/scripts/control_tanda0_en_152.py <w>/corridas/c152_1 <repo>/…/e0_chunking/salida_tanda0_r2b
python -B s0_5/scripts/manifiesto_salida_S0-5a.py <w>/corridas/c152_1 <w>/raices/repo/…/e0_chunking "<unidad>" <json>
# continuidad
python -B s0_5/scripts/control_continuidad_numeracion.py --e0 <w>/corridas/c152_1 --lineas <caché> --out <json>
python -B s0_5/scripts/lista_continuidad_S0-5a.py --antes s0_5/censos/control_continuidad_antes_S0-5a.json --despues <json> --out <md>
python -B s0_5/scripts/selftest_control_continuidad.py --antes <salida S0-4b> --despues <w>/corridas/c152_1 --lineas <caché>
# anclas de la tabla
python -B s0_5/b/scripts/anclas_e0_tabla_S0-5b.py <copia>/…/tabla_reprocesamiento.md <código de S0-4b> <copia>/…/e0_chunking --hasta 481
# paquete
python -B s0_5/b/scripts/verificar_manifest_S0-5b.py <paquete>
```
