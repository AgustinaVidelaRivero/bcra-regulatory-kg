# U-SEG-OFICIAL — REPORTE de S1-quater, fichas (13/10/2026)

El paso 3 del §9 del diseño de S1-quater, sus puntos 4 y 5: las fichas y los controles a ciegas. **Frené en el primer control a
ciegas:** en la etapa 1, una cuenta que tiene que dar 0 da 1 (§5). No miré el renglón. No corrí los otros controles del paso 4 ni el
paso 5. USD 0, sin API. Ningún id ni texto de unidades en este archivo ni en `s1quater/fichas/`. De las unidades, mis comandos
imprimieron solo sha256, cuentas, horas y nombres de archivo. La salida de los scripts que leen ids pasó por un filtro que reemplaza
lo que tenga forma de id (`<documento>::…`) por «un id», y el filtro no reemplazó nada.

## 1. Qué rige y con qué entradas

- **Diseño y adendas,** en HEAD (`git show HEAD:… | shasum -a 256`), con los sha256 de §1 del reporte del sorteo:
  `diseno_S1quater.md` `e4193377…`, `adenda_1` `8ce0ad8b…`, `adenda_2` `176fcd4d…`, `adenda_3` `16b36464…`, `adenda_4` `65dcc263…`.
- **Scripts,** copiados de HEAD (`git show HEAD:…`) al scratchpad, desde donde corrieron. Los cinco dan el sha256 del despacho:
  - `s1quater/diseno/scripts/fichas_S1quater.py` `7a980530…`, `comun_S1quater.py` `ade9df93…` y `prueba_S1quater.py` `ea20d911…`,
    con su salida sellada `salida_prueba_S1quater.txt` `c036a90b…`;
  - `s1ter/scripts/control_ciego_fichas_S1ter.py` `e56a89ef…` y `verificar_carpeta_lectora_S1ter.py` `23466eea…`.
- **Tres scripts más, que la prueba necesita:** `prueba_S1quater.py` importa `sorteo_S1quater.py` y corre `poblaciones_S1quater.py`
  (la versión 1) y `regresion_S1quater.py` desde su propia carpeta.
  - El despacho no los nombra. Los copié de HEAD a la misma carpeta.
  - Dan los sha256 de `s1quater/diseno/sello_diseno_S1quater.txt`: `9def8fed…`, `f0d51312…` y `5c1ebe63…`.
  - Solo los usó la prueba.
- **Dos scripts del sorteo,** copiados de HEAD y sin cambios: `s1quater/sorteo/scripts/control_e0_S1quater_sorteo.py` `463f79a5…`
  (paso 1) y `comparar_fotos_S1quater_sorteo.py` `9f68e61b…` (foto del repo).
- **Antes de leer los scripts** conté sus cadenas con `::`. Son código (`split("::")`, `RE_PARTE`) o ids inventados de la prueba
  (documento `d`). Ninguna es un id de la E0.
- **El orden sellado:** `NO_ABRIR_orden_lectura_S1quater.json`, del paquete de la ejecutora del sorteo. Da `b794f85f…`, el de
  `s1quater/sorteo/sello_sorteo_S1quater.txt`. No lo abrí: solo lo pasé como argumento. De ese paquete no leí ni listé nada más, y
  del paquete de la mesa, nada.
- **Python:** 3.10.13, el del `.venv` del repo, con `-B` y `PYTHONDONTWRITEBYTECODE=1`, en todos los scripts de esta unidad y del
  repo.
  - **Un desvío, error propio:** para cuatro tareas auxiliares usé el `python3` del sistema (3.12.13), con el script por la entrada
    estándar: editar el checkpoint, escribir el `manifest.txt` del paquete, resumir la salida de la comparación final de las fotos y
    mirar la salida de la prueba de mi control sobre la carpeta inventada.
  - **La causa:** lo escribí como `python3` por costumbre, en lugar de la ruta del `.venv`.
  - **El alcance:** ninguna de las cuatro corrió código del repo ni escribió en el repo, y un script leído por la entrada estándar no
    deja `.pyc`.

## 2. Paso 1: la E0 de 2374968a, en una copia

- **La copia:** `rsync -a --no-links --exclude=/.git --exclude=/.venv <repo>/ <scratchpad>/copia_repo/`, de 10:43:47 a 10:44:25.
  - Quedan 0 enlaces en la copia y 26.467 archivos.
  - rsync salteó 339 enlaces simbólicos: 336 de `data/experiment/ev2_corrida/navegabilidad/trazas_nav/` y 3 de `.venv-app/bin/`.
    Ninguno es insumo de E0 ni de S1-quater.
  - **El código de salida de esa pasada no quedó registrado:** lo tomé con una variable que la shell de la sesión no tiene. Una
    segunda pasada con `--itemize-changes`, a las 10:44:36, dio rc 0 y ningún cambio.
- **La raíz mínima:** `zsh <copia>/…/s0_4/scripts/raiz_minima.sh <copia> <scratchpad>/raiz_minima
  <copia>/data/experiment/reextraccion_v2/e0_chunking`, a las 10:44:47, con rc 0 y 0 enlaces.
  - Código de E0 en la raíz: `e0_lib.py` `d89aab1a…`, `correr_e0.py` `78c54c4c…`, `selftest_e0.py` `eb4f11e6…` y `e0_tablas.py`
    `ab300a22…`, los de §2 del reporte del sorteo.
  - `git diff --stat 2374968a HEAD` sobre el código de E0, los insumos que copia `raiz_minima.sh`, los scripts de S0-1 y S0-4 y el
    manifiesto de S0-6b da vacío, y `git status` no muestra cambios en esos insumos.
  - Los PDFs de `escalado_prep/pdfs/` no están en git. Los cubren el control de la E0 (abajo) y la prueba del diseño, que reproduce
    byte a byte las imágenes de S1-ter (§3).
- **La corrida:** `<copia>/…/s0_1/scripts/correr_152.py --codigo <raíz> --salida <scratchpad>/e0_152 --workers 8`, de 10:45:01 a
  10:49:16, con rc 0: «listo 152 TOs, 0 con error», 0 líneas `ERROR` y 769 entradas (los 768 archivos más `por_to/`).
- **El control** (`control_e0_S1quater_sorteo.py`; `controles/control_e0_S1quater_fichas.json`, 10:49:37):
  - el manifiesto `s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json` da `80adbd58…`, el del despacho;
  - están sus 768 archivos `e0/…`, sin faltantes ni sobrantes, y los 768 dan su sha256;
  - hay 152 TOs y **10.478 unidades**, con 0 TOs cuya cuenta difiera de `unidades_por_to`.
- **La E0 no va al paquete:** se rehace con estos comandos y su control.

## 3. Paso 2: la prueba del diseño

- **Las entradas, armadas con copias y sin enlaces:**
  - `--copia`: `<scratchpad>/prueba/copia/`, con `s1ter/` copiada de la copia del repo (con `e0/`; `diff -rq` contra la del repo:
    iguales) y `pdfs/` copiada de `escalado_prep/pdfs/` de la copia (152 PDFs);
  - `--s1ter-scripts` y `--planillas-s1ter`: `s1ter/scripts/` y `s1ter/tramo_b/` de HEAD, extraídas con `git archive HEAD … | tar -x`;
  - `--trabajo`: una carpeta nueva, que no abrí.
- **La corrida:** de 10:49:56 a 10:50:45, con rc 0 y nada en la salida de errores.
- **El resultado:** «30 de 30 casos ok»: 30 renglones `ok` y 0 `MAL`. La salida es igual byte a byte a la sellada (`cmp`; sha256
  `c036a90b87cec27f904c357faae7e7fc239efa6a53fe29e5aae9206efb4a4f0c`). Está en `controles/salida_prueba_S1quater_fichas.txt`.

## 4. Paso 3: las fichas

- **Comando:** `fichas_S1quater.py`, con los argumentos del despacho (§7), de 10:51:08 a 10:51:36, con rc 0. No frenó por «::».
- **Salidas:**
  - la carpeta `<scratchpad>/carpeta_lectora_S1quater/`, con `etapa_1/` y `etapa_2/`;
  - el registro `registro_fichas_S1quater.json` `5a46978779e277ec24636ce695c9d3f82c65a15596664508ce7235071f5bb31c`;
  - las planillas vacías `planilla_etapa_1_S1quater.tsv` y `planilla_etapa_2_S1quater.tsv`.
- **Control en cuentas** (`scripts/control_fichas_S1quater_fichas.py`; `controles/control_fichas_S1quater_fichas.json`, 10:51:54).
  Compara la carpeta, el registro y las planillas con el orden sellado:

  | etapa | fichas | imágenes | archivos | filas del `manifest.txt` | filas de la planilla |
  |---|---|---|---|---|---|
  | etapa_1 | 90 | 95 | 97 | 96 | 90 |
  | etapa_2 | 60 | 104 | 106 | 105 | 60 |

  - **Archivos:** cada etapa tiene sus imágenes, un archivo de fichas y el `manifest.txt` (95 + 1 + 1 = 97 y 104 + 1 + 1 = 106). El
    manifest lista todo menos a sí mismo (96 y 105).
  - **Fichas e imágenes:** las fichas van en el orden de los ids opacos, de `E1-001` a `E1-090` y de `E2-001` a `E2-060`, sin saltos.
    Cada ficha tiene al menos una imagen, y ninguna imagen está mal nombrada ni es de un id opaco ajeno.
  - **El registro:** coincide en fichas, imágenes, sha256 del `manifest.txt` y de cada archivo, y sha256 de cada planilla. Trae un
    número por ficha (90 y 60). No leí los números.
  - **Las planillas:** el encabezado de S1-ter, una fila por ficha en el orden de los ids opacos, y vacías todas las columnas salvo
    `ficha` y `paginas`.
  - **La prueba del control,** con una carpeta inventada (`scripts/prueba_control_fichas_S1quater_fichas.py`;
    `controles/salida_prueba_control_fichas_S1quater_fichas.txt`, 10:54:03): 8 de 8 casos ok. Da ok sobre la carpeta inventada y
    MAL en cada una de seis roturas, y frena con un orden que no da su sello.
  - **La prueba tuvo dos versiones.** La primera (su salida es de las 10:48:15, también 8 de 8) usaba en la carpeta inventada ids con
    forma de id de unidad. Para que `s1quater/fichas/` no tenga ninguna cadena así, los cambié por nombres sin «::» (el control no lee
    esos ids) y la volví a correr. La del repo es la segunda.
  - **El control no cambió después de su prueba:** su última modificación es de las 10:47:24 (`stat`), antes de la corrida sobre la
    carpeta real (10:51:54).
- **Sello:** `sello_fichas_S1quater.txt`, 10:52:09. Lleva el registro, los dos `manifest.txt` y las dos planillas (sha256 en §8).

## 5. Paso 4: el control a ciegas, y el freno

- **Comando:** `control_ciego_fichas_S1ter.py <carpeta> <copia>/…/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json <orden sellado>`,
  a las 10:52:29, con rc 0. El manifiesto de TOs da `f59cdea0…`, el de HEAD.
- **La salida:**
  - va entera a `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt`, en el paquete (sha256
    `6a41c24c55147d912dd6d79f4287e6e69e253a6eaf29b70a0a37e9506b93857d`);
  - tiene 6 renglones: 5 empiezan con `#` o `etapa_` y van a `controles/control_ciego_fichas_S1quater_cuentas.txt`; el otro no lo
    miré.
- **Las cuentas:**

  | etapa | fichas | renglones fuera del texto de la norma | con vocabulario de población, regla, tanda o límite | con un id de TO | «::» | ids de unidad | archivos ajenos | imágenes mal nombradas |
  |---|---|---|---|---|---|---|---|---|
  | etapa_1 | 90 | 1.054 | **1** | 0 | 0 | 0 | 0 | 0 |
  | etapa_2 | 60 | 870 | 0 | 0 | 0 | 0 | 0 | 0 |

- **El freno:** el despacho pide 0 renglones con ese vocabulario en las dos etapas, y en la etapa 1 hay 1. Frené sin mirarlo.
  - Cuando encuentra algo, el script imprime hasta cinco de esos renglones, con sangría. Con uno, imprime ese: es el único renglón
    de la salida que no empieza con `#` ni con `etapa_` (6 renglones = 1 de título + 2 por etapa + el encontrado).
  - No sé qué palabra lo marcó ni en qué parte de la ficha está. Tampoco lo busqué por otro camino.
- **Lo que no corrí,** por el freno:
  - `verificar_carpeta_lectora_S1ter.py`;
  - los comandos del paso 1 de la lectora;
  - el sello de los controles a ciegas (`sello_controles_ciegos_S1quater.txt`, que no existe);
  - el paso 5, salvo el tar (§6).

## 6. El tar de resguardo

- **Por qué:** la carpeta vive en el scratchpad, que el limpiador temporal de macOS borra a los tres días (CLAUDE.md §4.g), y es lo
  que se necesita para ver el freno.
- **Cómo:** con el comando del paso 5, a las 10:54:17:
  `COPYFILE_DISABLE=1 tar -C <scratchpad>/carpeta_lectora_S1quater -cf <paquete>/NO_ABRIR_carpeta_lectora_S1quater.tar etapa_1 etapa_2`.
- **Qué trae:** `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82`, 205 entradas: las 2 carpetas y 203 archivos
  (97 + 106).
- **Lo que no es:** no es la entrega del paso 5.
  - No lo extraje ni corrí sobre él `verificar_carpeta_lectora_S1ter.py`.
  - Su sha256 no está en el sello de las fichas.

## 7. Comandos

Las rutas `s0_1/…`, `s0_4/…`, `s0_6/…`, `s1ter/…` y `s1quater/…` son de `segmentacion_oficial_e0r2/`, en la copia.
`<orden>` es `NO_ABRIR_orden_lectura_S1quater.json`, en el paquete de la ejecutora del sorteo, con la ruta del despacho.
`<paquete>` es `revision_USEG_OFICIAL_FRENO_S1quater_fichas/`, en el scratchpad. `<head>` es `<scratchpad>/prueba/head`, con
`s1ter/scripts/` y `s1ter/tramo_b/` extraídas de HEAD (`git archive HEAD … | tar -x`). `PY` es el `python` del `.venv` del repo, siempre
con `PYTHONDONTWRITEBYTECODE=1` y `-B`.

```
rsync -a --no-links --exclude=/.git --exclude=/.venv <repo>/ <copia>/
zsh <copia>/…/s0_4/scripts/raiz_minima.sh <copia> <raíz> <copia>/data/experiment/reextraccion_v2/e0_chunking
PY -B <copia>/…/s0_1/scripts/correr_152.py --codigo <raíz> --salida <e0> --workers 8
PY -B <scratchpad>/scripts_sorteo/control_e0_S1quater_sorteo.py --e0 <e0> --manifest s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json --sha-manifest 80adbd58… --out <json>
PY -B <scratchpad>/scripts_s1quater/prueba_S1quater.py --copia <scratchpad>/prueba/copia --s1ter-scripts <head>/…/s1ter/scripts --planillas-s1ter <head>/…/s1ter/tramo_b --trabajo <scratchpad>/prueba/trabajo
PY -B <scratchpad>/scripts_s1quater/fichas_S1quater.py --orden <orden> --sha-orden b794f85f… --e0 <e0> --pdfs <copia>/data/experiment/escalado_prep/pdfs --out <scratchpad>/carpeta_lectora_S1quater --registro <scratchpad>/registro_fichas_S1quater.json --planillas <scratchpad>/planillas_S1quater
PY -B scripts/control_fichas_S1quater_fichas.py --carpeta <scratchpad>/carpeta_lectora_S1quater --registro <scratchpad>/registro_fichas_S1quater.json --planillas <scratchpad>/planillas_S1quater --orden <orden> --sha-orden b794f85f… --out <json>
PY -B scripts/prueba_control_fichas_S1quater_fichas.py --trabajo <carpeta nueva>
PY -B <scratchpad>/scripts_s1ter/control_ciego_fichas_S1ter.py <scratchpad>/carpeta_lectora_S1quater s1ter/manifiesto/segmentacion_oficial_e0r2_152.json <orden> > <paquete>/NO_ABRIR_control_ciego_fichas_S1quater_completo.txt
grep -E '^(#|etapa_)' <paquete>/NO_ABRIR_control_ciego_fichas_S1quater_completo.txt > controles/control_ciego_fichas_S1quater_cuentas.txt
COPYFILE_DISABLE=1 tar -C <scratchpad>/carpeta_lectora_S1quater -cf <paquete>/NO_ABRIR_carpeta_lectora_S1quater.tar etapa_1 etapa_2
find . -path ./.git -prune -o -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256 > <foto>     (desde la raíz del repo)
PY -B <scratchpad>/scripts_sorteo/comparar_fotos_S1quater_sorteo.py --antes <foto antes> --despues <foto después> --permitido ./data/experiment/segmentacion_oficial_e0r2/s1quater/fichas/ --out <json>
PY -B <copia>/…/s0_4/scripts/grep_convenciones.py <repo> <cada archivo de s1quater/fichas/>
```

En los argumentos van los sha256 enteros. Acá los abrevio a 8 caracteres; enteros están en los sellos y en §2 a §6.

## 8. Sellos

| sello | archivo | sha256 | hora |
|---|---|---|---|
| `sello_fichas_S1quater.txt` | `registro_fichas_S1quater.json` | `5a46978779e277ec24636ce695c9d3f82c65a15596664508ce7235071f5bb31c` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `etapa_1/manifest.txt` | `110565d7d8ceb555c41adbf56afbe784391e1b9e0c333a3a434a392abf02f423` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `etapa_2/manifest.txt` | `37580fbc61eae04809b2c8d4e7606885aea333c833429294f35e9d60f9f13c1c` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `planilla_etapa_1_S1quater.tsv` | `9daf0e2319e3a3e65c39cccbc1d99f68b2e81fadf222519eb097847b0ea2e898` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `planilla_etapa_2_S1quater.tsv` | `d450d5ddd4b6c6aeb64fe55c01278646a790ac440c72fe59537d081b9653f818` | 10:52:09 |

Todas las horas son del 13/10/2026, -0300. El sello de los controles a ciegas no existe: el freno llegó antes (§5).

## 9. Repo, `.pyc`, convenciones y archivos con texto o ids

- **Repo:** foto sha256 del repo entero (sin `.git` y sin ninguna otra exclusión), con `find` y `shasum`.
  - Antes, de 10:42:10 a 10:42:33: 50.061 archivos.
  - La de después y su comparación van en el FRENO. Las dos fotos enteras están en el paquete.
- **`.pyc`:** antes, 10.158 en todo el repo y 2.213 fuera de `.venv/`. El de después va en el FRENO.
- **Grep de convenciones:** el resultado va en el FRENO y en `controles/grep_convenciones_S1quater_fichas.txt`.
- **Archivos con texto o ids, en el paquete:** `NO_ABRIR_carpeta_lectora_S1quater.tar` y
  `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt`. Los escribieron `tar` y el script, y no los abrí.
- **Los otros archivos del paquete con datos de las fichas:**
  - el registro trae el número que la segmentación le asignó a cada ficha, por id opaco (lo dice `fichas_S1quater.py`);
  - las planillas traen los ids opacos y las páginas.
  - No traen ids de unidades ni texto. No los abrí: los conté y los leyó mi script de control.
- **Rutas en lo que guardo:** `<repo>`, `<scratchpad>`, `<copia>` y `$HOME` en lugar de las rutas de la sesión.
- **Lo que no hice:** no escribí en la memoria ni en `.claude/`, no usé esperas programadas, no commiteé y no preparé ningún mensaje
  de commit.

## Tramo 2, después del seguí

El seguí de la mesa (hoja de ruta de la mesa, §87) declara falsa alarma el renglón del §5 y pide completar el paso 4 y el paso 5.
Todo corrió con el `python` del `.venv` del repo (3.10.13), con `-B` y `PYTHONDONTWRITEBYTECODE=1`, también en las tareas auxiliares.
El checkpoint lo edité con el editor, sin `python`. No se dio ninguna de las condiciones de freno del seguí (puntos 1 y 2).

### T1. La carpeta, igual a su sello (13:12:27)

- **La carpeta:** sigue en el scratchpad, en `<scratchpad>/carpeta_lectora_S1quater/`, así que no hizo falta extraerla del tar.
- **Sus manifest:** `etapa_1/manifest.txt` da `110565d7…` y `etapa_2/manifest.txt` da `37580fbc…`, los de `sello_fichas_S1quater.txt`.
- **El registro y las planillas:** los controlé solo por sha256, en el scratchpad y en el paquete. Dan los del sello.

### T2. Lo que faltó del paso 4 (13:12:42)

- **El control a ciegas no lo volví a correr.** Vale su salida de las 10:52:29 (`6a41c24c…`).
- **`verificar_carpeta_lectora_S1ter.py <carpeta>`:** rc 0. «96 de 96» en la etapa 1 y «105 de 105» en la etapa 2, nada sin listar,
  ningún `.DS_Store` y nada en la raíz (`controles/verificar_carpeta_lectora_S1quater.txt`).
- **Los comandos del paso 1 de la lectora** (`awk 'NR>2 && NF{print $1"  "$3}' manifest.txt | shasum -a 256 -c -`, desde cada etapa):
  - etapa 1: 96 OK y 0 no OK, rc 0; etapa 2: 105 OK y 0 no OK, rc 0;
  - las cuentas están en `controles/paso1_lectora_S1quater_cuentas.txt`;
  - la lista entera tiene un renglón por archivo, con los ids opacos y las páginas de las imágenes. Va al paquete como
    `NO_ABRIR_paso1_lectora_S1quater_completo.txt`. Imprimí solo las cuentas.

### T3. El paso 5: el tar, rehecho y verificado (13:13:09)

- **Rehecho** con el comando del despacho, sobre el de resguardo:
  `COPYFILE_DISABLE=1 tar -C <scratchpad>/carpeta_lectora_S1quater -cf <paquete>/NO_ABRIR_carpeta_lectora_S1quater.tar etapa_1 etapa_2`
  (rc 0).
- **Su sha256:** `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82`, el mismo que el de resguardo. Ningún archivo
  de la carpeta cambió entre los dos tar.
- **Verificado:**
  - **las entradas:** 205, 2 carpetas y 203 archivos;
  - **la extracción:** en una carpeta nueva, `<scratchpad>/tramo2/extraccion_tar/`, con rc 0 y 0 enlaces;
  - **`verificar_carpeta_lectora_S1ter.py` sobre la extracción:** rc 0, salida igual byte a byte a la de T2 (`cmp`;
    `controles/verificar_carpeta_lectora_S1quater_tar.txt`);
  - **`diff -rq` entre la carpeta y la extracción:** rc 0 y 0 renglones.

### T4. El sello de los controles a ciegas (13:13:31)

`sello_controles_ciegos_S1quater.txt`. Lleva, cada uno con la hora de su salida:

| archivo | dónde | sha256 | hora de la salida |
|---|---|---|---|
| `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt` | paquete | `6a41c24c55147d912dd6d79f4287e6e69e253a6eaf29b70a0a37e9506b93857d` | 10:52:29 |
| `controles/control_ciego_fichas_S1quater_cuentas.txt` | repo | `9ce27b048d0dbc1ca57ff74c69b6e5c8138c3f15b3629973d12c838acb3936bc` | 10:52:29 |
| `controles/verificar_carpeta_lectora_S1quater.txt` | repo | `a6f2b61e15afa4700ac13a88ef6b2ee13fb1d0f244fa94689bef64c8db5860f4` | 13:12:42 |
| `controles/paso1_lectora_S1quater_cuentas.txt` | repo | `4c3ad99fb395305407106f25b504007887fd95f4d9add44b3855aa0d61a90bd8` | 13:12:42 |
| `NO_ABRIR_paso1_lectora_S1quater_completo.txt` | paquete | `e1c105a68c0015bc864bdabe841e0a4fae8dc44f183d191fde32c8db165505e9` | 13:12:42 |
| `controles/verificar_carpeta_lectora_S1quater_tar.txt` | repo | `a6f2b61e15afa4700ac13a88ef6b2ee13fb1d0f244fa94689bef64c8db5860f4` | 13:13:09 |
| `NO_ABRIR_carpeta_lectora_S1quater.tar` | paquete | `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82` | 13:13:09 |

- **El sello de las fichas no lo toqué.** El sha256 del tar va en este sello y no en aquel, como pide el seguí.
- **Los dos `verificar` dan el mismo sha256** porque su salida es la misma.

### T5. Lo que declaro

- **El renglón del §5.**
  - **Qué es:** 1 renglón de la etapa 1, en el rótulo del número que la segmentación le asignó a una ficha.
  - **Qué lo marcó:** el término de la lista que coincide es `1\.16`. Cae en el número, que viene de la E0, y no en la parte fija
    del rótulo. Según la E0, `1.16` está también en el texto propio y en la herencia de la unidad.
  - **El veredicto:** falsa alarma, por la regla de la autora, fijada antes del diagnóstico (hoja de ruta de la mesa, §87). Si el
    término está en el texto de la unidad o en su herencia, como los da la E0, la alarma es falsa: se declara y se sigue.
  - **Quién lo diagnosticó:** la mesa, por script.
  - **Lo que no verifiqué:** el diagnóstico lo tomo del seguí de la mesa. **NO VERIFICADO en esta sesión:** verificarlo exige leer
    el renglón o la ficha.
  - **Nadie lo miró:** yo no miré el renglón ni lo busqué, por ningún camino. La salida entera del control a ciegas sigue sin abrir.
- **Los tres scripts del diseño que necesitó la prueba:** `sorteo_S1quater.py`, `poblaciones_S1quater.py` y `regresion_S1quater.py`.
  El despacho no los nombraba: la omisión es del despacho. Los copié de HEAD y dan los sha256 de `sello_diseno_S1quater.txt` (§1).
- **El `python3` del sistema** (3.12.13): lo usé en el primer tramo en cuatro tareas auxiliares fuera del repo (§1). En este tramo
  usé solo el del `.venv`.
- **El registro y las planillas vacías:** los trato como `NO_ABRIR_`, sin cambiarles el nombre, porque el sello de las fichas los
  nombra así. En este tramo solo los controlé por sha256.
- **El `sleep 60` del primer tramo:**
  - **Qué hice:** mientras corría la E0, escribí un `sleep 60` seguido de un `cat` de la salida de la tarea, para esperarla. Fue un
    error: el despacho pide dejar que la tarea en segundo plano avise sola.
  - **Qué pasó:** la herramienta de la sesión bloqueó el comando antes de correrlo. No hubo espera ni `cat`.
  - **Contra el seguí:** el seguí lo describe como una espera activa. Fue un intento de espera activa, que no llegó a correr.
  - **En este tramo:** ninguna espera.

### T6. Repo, `.pyc`, convenciones y paquete

- **Foto sha256 del repo antes de este tramo:** de 13:11:25 a 13:11:48, 50.073 archivos, igual a la foto final del primer tramo
  (`cmp`).
- **La foto de después, su comparación, los `.pyc` y el grep** van en `FRENO_S1quater_fichas_tramo_2.md`. Las salidas nuevas son
  `controles/comparar_fotos_S1quater_fichas_tramo_2.json` y `controles/grep_convenciones_S1quater_fichas_tramo_2.txt`.
- **El paquete, actualizado:**
  - el tar rehecho reemplaza al de resguardo, con el mismo sha256;
  - suma la lista entera del paso 1 de la lectora, las fotos del tramo y la copia actualizada de `s1quater/fichas/`.
- **Archivos del paquete con texto o ids,** escritos por `tar` y por los comandos, sin abrirlos:
  - `NO_ABRIR_carpeta_lectora_S1quater.tar`;
  - `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt`;
  - `NO_ABRIR_paso1_lectora_S1quater_completo.txt`;
  - el registro y las dos planillas, que trato como `NO_ABRIR_`.
