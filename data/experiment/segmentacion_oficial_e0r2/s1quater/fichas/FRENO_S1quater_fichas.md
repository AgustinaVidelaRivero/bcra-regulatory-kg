# U-SEG-OFICIAL — FRENO de S1-quater, fichas (13/10/2026)

El paso 3 del §9 del diseño, sus puntos 4 y 5: las fichas y los controles a ciegas. **Frené en el primer control a ciegas: en la
etapa 1, 1 renglón con vocabulario de población, regla, tanda o límite, donde el despacho pide 0.** No lo miré. Las demás cuentas de
ese control dan 0. No corrí los otros controles del paso 4 ni el paso 5, salvo el tar de la carpeta, que guardé como resguardo.
Hasta ahí, todo dio lo que fija el despacho. USD 0, sin API. Ningún id ni texto de unidades en `s1quater/fichas/`. **Nada
commiteado, ningún mensaje de commit preparado, nada escrito en la memoria.** El detalle y los comandos están en
`REPORTE_S1quater_fichas.md`.

## Paso 0 (con `$HOME`)

Lo corrí antes de cualquier otro comando, antes de la foto del repo de las 10:42:10. No registré su hora.

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --oneline -1
cc60a4b4 Segmentacion oficial: el sorteo de la lectura de la E0 corregida, con sus sellos y controles
$ git status --porcelain -- data/experiment/reextraccion_v2/e0_chunking data/experiment/segmentacion_oficial_e0r2/s1quater data/experiment/segmentacion_oficial_e0r2/s1ter
?? data/experiment/segmentacion_oficial_e0r2/s1ter/e0/
$ shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298  data/experiment/reextraccion_v2/e0_chunking/e0_lib.py
78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e  data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
eb4f11e61981476957aceadb67bfbf80934c8f903c11760b41fc2530bbe38282  data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
$ ls data/experiment/segmentacion_oficial_e0r2/s1quater
diseno
sorteo
```

- **Contra el despacho:** todo igual. Los tres sha256 son los «después» de `s0_6/bis/parche/LEEME.md`.
- **Lo que rige, en HEAD:** el diseño y las cuatro adendas dan los sha256 del reporte del sorteo, §1. Los cinco scripts del despacho
  y la salida sellada de la prueba dan los suyos.
- **Tres scripts del diseño que el despacho no nombra:** `prueba_S1quater.py` importa `sorteo_S1quater.py` y corre
  `poblaciones_S1quater.py` y `regresion_S1quater.py` desde su carpeta. Los copié de HEAD junto a ella. Dan los sha256 de
  `sello_diseno_S1quater.txt`.
- **El orden sellado:** da `b794f85f…`, el de `sello_sorteo_S1quater.txt`. Lo pasé solo como argumento, sin abrirlo.

## Paso 1: la E0 contra su manifiesto

- **La copia:** con `rsync -a --no-links`, sin `.git` ni `.venv`, con 0 enlaces (se saltearon 339, ajenos a E0). De ella armé la raíz
  mínima con `raiz_minima.sh`, también con 0 enlaces, con el código de E0 de `2374968a`.
  - El código de salida de la primera pasada de rsync no quedó registrado. Una segunda pasada dio rc 0 y ningún cambio (REPORTE, §2).
- **La corrida:** `correr_152.py --workers 8`, de 10:45:01 a 10:49:16, con rc 0, 152 TOs y 0 con error.
- **El control** (10:49:37; `controles/control_e0_S1quater_fichas.json`): `manifest_salida_e0_152_S0-6b.json` da `80adbd58…`. **Están
  sus 768 archivos `e0/…`, los 768 dan su sha256**, sin faltantes ni sobrantes, con **10.478 unidades** y 152 TOs, y ningún TO con
  otra cuenta.

## Paso 2: la prueba del diseño

- **La corrida:** de 10:49:56 a 10:50:45, con rc 0.
- **El resultado:** **«30 de 30 casos ok»**, 0 `MAL`.
- **Contra la sellada:** igual byte a byte (`cmp`; `c036a90b87cec27f904c357faae7e7fc239efa6a53fe29e5aae9206efb4a4f0c`).

## Paso 3: las fichas

- **La corrida:** `fichas_S1quater.py`, de 10:51:08 a 10:51:36, con rc 0. No frenó por «::».
- **Las cuentas** (`scripts/control_fichas_S1quater_fichas.py`; `controles/control_fichas_S1quater_fichas.json`, todo ok):

  | etapa | fichas | imágenes | archivos (imágenes + fichas + manifest) | filas del `manifest.txt` | filas de la planilla vacía |
  |---|---|---|---|---|---|
  | etapa_1 | 90 | 95 | 97 | 96 | 90 |
  | etapa_2 | 60 | 104 | 106 | 105 | 60 |

  - **Fichas e imágenes:** los ids opacos van seguidos, de `E1-001` a `E1-090` y de `E2-001` a `E2-060`, en el orden sellado. Cada
    ficha tiene su imagen, y no hay imágenes mal nombradas ni archivos ajenos.
  - **Registro y planillas:** el registro coincide con la carpeta y con las planillas. Las planillas solo traen `ficha` y `paginas`.
  - **El control, probado** con una carpeta inventada: 8 de 8 casos ok.

## Paso 4: el control a ciegas, y el freno

`control_ciego_fichas_S1ter.py`, a las 10:52:29, con rc 0. Lo que empieza con `#` o con `etapa_`
(`controles/control_ciego_fichas_S1quater_cuentas.txt`), en tabla:

| etapa | fichas | renglones fuera del texto de la norma | con vocabulario de población, regla, tanda o límite | con un id de TO | «::» | ids de unidad | archivos ajenos | imágenes mal nombradas |
|---|---|---|---|---|---|---|---|---|
| etapa_1 | 90 | 1.054 | **1** | 0 | 0 | 0 | 0 | 0 |
| etapa_2 | 60 | 870 | 0 | 0 | 0 | 0 | 0 | 0 |

- **El renglón:** la salida tiene 6 renglones: el título, dos por etapa y uno más. Ese otro es el renglón que el script encontró. No
  lo miré: la salida entera está en `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt`, en el paquete.
- **Lo que no sé:** no sé qué palabra lo marcó ni en qué parte de la ficha está. No lo busqué por otro camino.
- **Lo que no corrí:**
  - `verificar_carpeta_lectora_S1ter.py`;
  - los comandos del paso 1 de la lectora;
  - el sello de los controles a ciegas;
  - el paso 5, salvo el tar.
- **El tar** (10:54:17): `NO_ABRIR_carpeta_lectora_S1quater.tar` `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82`,
  con el comando del paso 5. Trae 205 entradas: 2 carpetas y 203 archivos.
  - Va al paquete como resguardo, porque el scratchpad se borra a los tres días.
  - No es la entrega del paso 5: no lo extraje ni lo verifiqué, y su sha256 no está en el sello de las fichas.
- **Lo decide la mesa.**

## Sellos

| sello | archivo | sha256 | hora |
|---|---|---|---|
| `sello_fichas_S1quater.txt` | `registro_fichas_S1quater.json` | `5a46978779e277ec24636ce695c9d3f82c65a15596664508ce7235071f5bb31c` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `etapa_1/manifest.txt` | `110565d7d8ceb555c41adbf56afbe784391e1b9e0c333a3a434a392abf02f423` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `etapa_2/manifest.txt` | `37580fbc61eae04809b2c8d4e7606885aea333c833429294f35e9d60f9f13c1c` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `planilla_etapa_1_S1quater.tsv` | `9daf0e2319e3a3e65c39cccbc1d99f68b2e81fadf222519eb097847b0ea2e898` | 10:52:09 |
| `sello_fichas_S1quater.txt` | `planilla_etapa_2_S1quater.tsv` | `d450d5ddd4b6c6aeb64fe55c01278646a790ac440c72fe59537d081b9653f818` | 10:52:09 |

- **Las horas:** todas del 13/10/2026, -0300.
- **El orden:** el sello de las fichas se escribió después del control de las fichas y antes del control a ciegas.
- **El sello de los controles a ciegas** no existe, por el freno.

## Repo, `.pyc` y convenciones

- **Foto sha256 del repo entero (sin `.git` y sin otra exclusión),** con `find … | shasum -a 256`:
  - antes, de 10:42:10 a 10:42:33: 50.061 archivos;
  - después, de 10:56:34 a 10:56:57: 50.070 archivos.
  - **La comparación** (`comparar_fotos_S1quater_sorteo.py` de HEAD; `controles/comparar_fotos_S1quater_fichas.json`): **9 archivos
    nuevos, todos en `s1quater/fichas/`. Fuera de esa carpeta, 0 nuevos, 0 cambiados y 0 borrados.**
  - **Lo que entró después de la foto:** este FRENO y la salida del grep, en `s1quater/fichas/`. La comparación final, hecha después
    de escribirlos, va en el mensaje del FRENO. Las dos fotos enteras están en el paquete.
- **`.pyc`:** 10.158 en todo el repo y 2.213 fuera de `.venv/`, antes y después. Todo corrió con `-B` y `PYTHONDONTWRITEBYTECODE=1`,
  desde el scratchpad y la copia.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre los archivos de `s1quater/fichas/` sin contar el suyo): el
  resultado está en `controles/grep_convenciones_S1quater_fichas.txt` y en el mensaje del FRENO.

## Archivos del paquete con texto o ids (escritos por `tar` y por el script, sin abrirlos)

- `NO_ABRIR_carpeta_lectora_S1quater.tar` `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82`: las fichas y las
  imágenes, con el texto de las 90 y las 60 unidades.
- `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt` `6a41c24c55147d912dd6d79f4287e6e69e253a6eaf29b70a0a37e9506b93857d`: trae el
  renglón encontrado.
- **Sin texto ni ids de unidades, pero con datos de las fichas:**
  - el registro trae el número que la segmentación le asignó a cada ficha;
  - las planillas traen los ids opacos y las páginas.

## Escrituras

- **En el repo:** solo `s1quater/fichas/`, que es nueva. Tiene este FRENO, el REPORTE, el sello de las fichas, dos scripts en
  `scripts/` y los controles en cuentas en `controles/`.
- **Fuera del repo:** el scratchpad de la sesión y el paquete `revision_USEG_OFICIAL_FRENO_S1quater_fichas/`, con su copia en
  `fuera_del_repo/scratchpads/`. La ruta de la copia y su verificación van en el mensaje del FRENO.

FRENO.
