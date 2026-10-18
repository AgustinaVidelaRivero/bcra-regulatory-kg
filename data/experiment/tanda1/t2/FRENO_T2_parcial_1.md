# FRENO T2 (parcial) — tanda 1 de B6.1: la extracción E1 a E3 frenó por proyección en el segundo TO (16/10/2026, sin commit)

Rigen el §2, el §3, el §4.2 y el §7 del pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`). HEAD `ea61cfdb`. Lancé
T2 una sola vez, desde esta sesión. **El lanzador salió con 3, un freno del runner:**

```
FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21
```

- **Lo que se hizo:** ri_gerc completo; ri_pgn con E1 y E3 cerradas y sin su E2. Los otros 18 TOs no empezaron.
- **El gasto:** USD 1,149063 de un tope de 100,7291.
- **Lo que no hice:** no relancé y no subí el tope. Decide la autora (§4.2: «si la estimación revisada supera el tope, se frena y se
  pregunta; no se recorta en silencio ningún documento»).
- Nada commiteado y ningún mensaje de commit preparado. El commit es de la autora y queda PENDIENTE.

## 1. Paso 0 (20:46:31)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git log -3 --format='%h %s'
ea61cfdb Registro de decisiones: la primera tanda antes de su extraccion
9d1cdd92 Primera tanda: la corrida en seco, la segmentacion de sus veinte documentos y el manifiesto de la extraccion
73f86f4b Registro de decisiones: la etapa corta del sistema por fragmentos y las firmas del laudo y del pre-registro de la primera tanda
$ git status --porcelain --untracked-files=no
$ git ls-files data/experiment/tanda1 data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json | wc -l
     147
$ shasum -a 256 -c data/experiment/tanda1/t1/sha256_para_T2.txt | awk '{print $NF}' | sort | uniq -c
 108 OK
$ shasum -a 256 -c data/experiment/tanda1/t1/sha256_para_T2.txt | grep -v ': OK$' | wc -l
       0
$ shasum -a 256 data/experiment/tanda1/t1/sha256_para_T2.txt
1793a70e99457a1addb55ff00c45cd911cf0a33345a406dea4aaaf1b99594a0e  data/experiment/tanda1/t1/sha256_para_T2.txt
$ pgrep -fl "runner_corpus.py|lanzar_t2.py"
```

- `git status` salió vacío, y `pgrep` también (rc 1).
- `data/experiment/reextraccion_v2/corpus_tanda1/` y `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_1` no
  existían.
- `df -k .`: 187.009.224 KB libres en `/System/Volumes/Data`.
- El piso y las 78 rutas los controló el lanzador (sección 2, renglón `controles_previos`).
- **La foto antes** (20:47:34 a 20:47:45): 51.198 entradas, 14 sin abrir y 342 enlaces. La sacó `t2/foto_repo_tanda1_t2.py`, que es nuevo:
  - es la foto de T1 con un agregado: las bases del runner y `logs/cache_usage.jsonl` van solo por tamaño y fecha, sin abrirse;
  - el log de uso, porque sus líneas por componente contarían los reintentos;
  - lo escribí antes de la foto.
- **Los `.pyc`:** 11.236 líneas.

## 2. El lanzamiento

Desde la raíz del repo, en segundo plano (`run_in_background` del Bash), una sola vez, sin `--stub`, `--solo-tos` ni `--git-repo`:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_1"
```

- **Inicio:** 20:48:13 (`inicio_lanzador`, pid 76009). **Fin:** 21:01:43 (`fin_lanzador`). Duró 13,5 min.
- **Código de salida: 3.** La app avisó «exited with code 3»; caffeinate devuelve el del lanzador.
- **`controles_previos`** (20:48:14), todo OK:
  - el piso: 186.976.748 KB libres, contra 31.457.280;
  - las rutas: `HEAD:  78 de 78`, `árbol: 78 de 78`;
  - el SDK: `0.100.0`;
  - el sha256 y el tope del manifiesto;
  - la carpeta de trabajo, fuera del repo y nueva.
- **`freno_modelo_antes`** (20:48:15): OK, con los ids vacíos porque todavía no había filas.
- **Por TO** (`avance_t2.jsonl`, sha256 `dd812538…`):

| TO | inicio | fin | min | rc | freno por modelo | ids de E1 | ids de E3 | gasto global USD |
|---|---|---|---:|---:|---|---|---|---:|
| ri_gerc | 20:48:15 | 20:51:33 | 3,3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0,352899 |
| ri_pgn | 20:51:33 | 21:01:43 | 10,2 | 3 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |

- **El último renglón:** `{"evento": "fin_lanzador", "ts": "2026-10-16T21:01:43-0300", "copia_de_las_bases_borrada": true}`. Lo precede la
  `parada` «el runner salió con 3 en ri_pgn» (21:01:43). El lanzador no empezó el TO siguiente.
- **La copia de trabajo de las bases:** borrada (`ls` de `bases_lanzamiento_1`: «No such file or directory»). La carpeta de arriba,
  `fuera_del_repo/trabajo_t2_tanda1/`, quedó vacía.

## 3. La salida de `resumen_t2.py`, completa

`.venv/bin/python -B data/experiment/tanda1/t2/resumen_t2.py --repo . --out data/experiment/tanda1/t2/resumen_t2.json` (rc 0;
`resumen_t2.json`, sha256 `452f4aa5…`):

```
TO          unid c/part  acept  cola  err s/dest idsrep  cob cobE0     gasto
ri_gerc       15     15     15     0    0      0      0    T     T    0.3529
ri_pgn        21     21     20     1    0      0      0    T     T    0.7962
ceninf        39     39      0     0    0     39      0    F     T    0.0000
ri_rml        46     46      0     0    0     46      0    F     T    0.0000
nmcief        55     55      0     0    0     55      0    F     T    0.0000
adrei         70     70      0     0    0     70      0    F     T    0.0000
opefci        74     74      0     0    0     74      0    F     T    0.0000
ri_dcpc       75     75      0     0    0     75      0    F     T    0.0000
snp_tr       103    103      0     0    0    103      0    F     T    0.0000
efemin       119    119      0     0    0    119      0    F     T    0.0000
ri_mmsef     128    128      0     0    0    128      0    F     T    0.0000
manori       152    152      0     0    0    152      0    F     T    0.0000
expaef       165    165      0     0    0    165      0    F     T    0.0000
ri_ccna      169    169      0     0    0    169      0    F     T    0.0000
ayccef       196    196      0     0    0    196      0    F     T    0.0000
cirmo3       256    256      0     0    0    256      0    F     T    0.0000
snp_cheq     265    265      0     0    0    265      0    F     T    0.0000
cajasc       287    287      0     0    0    287      0    F     T    0.0000
depaho       442    442      0     0    0    442      0    F     T    0.0000
lingeef      613    613      0     0    0    613      0    F     T    0.0000
total       3290   3290     35     1    0   3254      0
gasto global USD 1.1491 de un tope de USD 100.7291 (dentro del tope); TOs con las dos fases cerradas: 2
[ri_gerc] corrida completa: gasto global=USD 0.3529 | wall=3.3 min
[ri_pgn] FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21
```

- **En los dos TOs que corrieron:** 36 unidades, 35 aceptadas, 1 en cola y 0 errores; cobertura completa, 0 ids repetidos y la cobertura
  exacta de la E0.
- Los otros 18 no empezaron: sus 3.254 unidades salen «sin destino».

## 4. La salida de `conteos_t2.py` y los `NO_ABRIR_`

`.venv/bin/python -B data/experiment/tanda1/t2/conteos_t2.py --repo .` (rc 0):

```
sha256 524c4b84a121516a60bb4d14a048dc2c50e526a38da400020531e709b0908d65
vigilancia integridad_e3: OK
```

El sha256 de los dos `NO_ABRIR_`, que no abrí:

```
d3e9d63777dfc1676061ba3cf51482f9ae6fb6ae0282c0876e2f5709ea97e2d5  data/experiment/tanda1/t2/NO_ABRIR_salida_e3_tanda1.txt
524c4b84a121516a60bb4d14a048dc2c50e526a38da400020531e709b0908d65  data/experiment/tanda1/t2/NO_ABRIR_conteos_reextracciones_tanda1.json
```

## 5. La causa: el freno por proyección

**El freno.** El runner proyecta el total al cierre de cada fase (`checkpoint`, `runner_corpus.py:433-451`, llamado al cerrar E3 en `:947`):
el gasto real más el estimado restante, por un factor que es la razón entre lo real y lo estimado de lo ya pagado
(`proyeccion`, `:400-430`). Lo reproduje con `estado_corpus.json` (solo los gastos totales) y el manifiesto:

| | USD |
|---|---:|
| gasto real (ri_gerc y ri_pgn, sus cuatro fases) | 1,149063 |
| estimado de esas cuatro fases | 0,766717 |
| razón = factor | 1,4987 |
| estimado total del runner (redondeado a 3 decimales) | 69,659 |
| estimado restante | 68,661703 |
| **proyección** = 1,149063 + 1,4987 × 68,661703 | **104,0509** |
| tope | 100,7291 |

- **Por TO:** ri_gerc costó 0,352899 contra 0,319465 estimados (1,1047 veces), y ri_pgn, 0,796164 contra 0,447252 (1,7801 veces).
- **Por unidad:** las 36 unidades costaron 0,031918 cada una, contra la tarifa de 0,021115 más las líneas de alcance.
- **El orden de corrida** de menor a mayor se eligió para que el freno por proyección actúe con poco gasto, y así actuó: con 1,14 % del tope.

**Una observación sobre el código sellado** (no es la causa). En el checkpoint de cierre, la fase que cierra entra dos veces en el estimado
corrido: una porque ya está en `fases_cerradas` y otra como `fase_key` con fracción 1 (`:404-415`; `cerrar_fase` va antes del checkpoint,
`:945-947`). El estimado restante baja en 0,230580 (el e3 de ri_pgn). Sin esa doble cuenta, la proyección da 104,3965 en lugar de 104,0509:
es un poco menos conservadora. No toqué nada: es una de las 78 rutas.

**El estado en disco** (`estado_corpus.json`):
- las cuatro fases cerradas: ri_gerc:e1, ri_gerc:e3, ri_pgn:e1 y ri_pgn:e3;
- `fase_actual` en null.
- El E2 de ri_pgn no corrió, porque el freno saltó dentro de `fase_e3`, antes de `cerrar_e2` (`:1438-1446`). Por eso su carpeta no tiene
  grafos.
- Ningún pedido de los 18 TOs que faltan se hizo.

**Qué haría un relanzamiento con el mismo tope.** Esto es lectura del código, no lo corrí:
- saltea las cuatro fases cerradas;
- corre el E2 de ri_gerc otra vez, que es offline y determinístico, y el de ri_pgn por primera vez;
- empieza ceninf:e1, porque el margen antes de cada unidad pasa (1,149 + 0,35 < 100,73);
- vuelve a proyectar al cerrar ceninf:e1, ya que ceninf no tiene checkpoints intermedios;
- y frena otra vez si gasto real + razón × estimado restante pasa 100,7291. Con los números de hoy, eso es una razón de más de
  (100,7291 − 1,149063) / 68,661703 = 1,4503; el umbral exacto al cerrar ceninf:e1 depende de lo que cueste ceninf.
- Lo ya pagado sale de la caché (`runner_corpus.py:787-788`, `:898`, `:1401`, `:1422`).

## 6. Gasto y duración contra lo proyectado

- **Gasto:** USD 1,149063 en 2 de 20 TOs y 36 de 3.290 unidades. Contra el estimado de esos dos TOs (0,766717) es 1,4987 veces; contra el
  estimado de la tanda (69,6592), 1,65 %; contra el tope (100,7291), 1,14 %.
- **Duración:** 13,5 min para 36 unidades, unos 22,4 s por unidad (de 20:48:15 a 21:01:43). La tanda 0 corrió a 11,84 s por unidad, con la
  que se proyectaron ~649 min para las 3.290. Dos TOs chicos no alcanzan para corregir esa proyección.

## 7. La foto del repo, los .pyc y el grep de convenciones

- **La foto** (`foto_repo_tanda1_t2.py`). Antes: 20:47:34 a 20:47:45, 51.198 entradas. Después: 21:03:33 a 21:03:44, 51.231 entradas.
  - **35 nuevos:** 31 en `reextraccion_v2/corpus_tanda1/` (16 de ri_gerc, 8 de ri_pgn, 4 checkpoints, `estado_corpus.json`,
    `presupuesto_compartido.json` y `ultimo_checkpoint.json`) y 4 en `tanda1/t2/` (`avance_t2.jsonl`, `resumen_t2.json` y los dos
    `NO_ABRIR_`). Ninguno en otra ruta.
  - **2 borrados:** `e1_extractor/cache/e1_extraccion.db-shm` (32.768 bytes) y `-wal` (0 bytes), que SQLite saca al cerrar la base.
  - **4 cambiados, solo por tamaño y fecha:**
    - `e1_extraccion.db`: de 406.601.728 a 410.034.176 bytes;
    - `e1_reintentos.db`: de 54.136.832 a 54.325.248;
    - `e3_verificacion.db`: de 266.383.360 a 267.808.768;
    - `logs/cache_usage.jsonl`: de 3.912.196 a 3.929.020. Este no está en la lista de lo nuevo del «seguí»: es el log de uso de cada
      respuesta real, que los clientes escriben en la raíz del repo (`cliente_e1.py:53`, `cliente_e3.py:52`; decisión D3 de caching). No
      lo abrí.
  - **Además**, nuevos en `t2/` respecto de HEAD: `foto_repo_tanda1_t2.py`, escrito antes de la foto, y este FRENO, escrito después.
  - `git status --porcelain --untracked-files=no` sigue vacío.
- **Los `.pyc`:** 11.236 antes y 11.236 después, iguales (`diff` vacío).
- **El grep de convenciones** (los tokens de `git config user.name` más los de mensajes, con `grep -c -i -E`), sobre lo nuevo de `t2/` sin
  los `NO_ABRIR_` (`FRENO_T2.md`, `foto_repo_tanda1_t2.py`, `avance_t2.jsonl` y `resumen_t2.json`). Lo que da, con el control positivo, va
  en el mensaje del FRENO.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna, `gold_q12_ajuste/` incluida. No hice ninguna copia del repo en T2.

## 8. Errores propios, con su causa

1. **Un archivo en `/tmp`.** En el paso 0 mandé una salida de `shasum -c` a `/tmp/_no_usar`, fuera del scratchpad: un descuido al redirigir
   una prueba. Lo borré enseguida (`ls` da «No such file or directory»). No quedó nada en `/tmp`.
2. **Un `ls` de más.** Para ver qué quedó en disco después del freno corrí `ls` de la carpeta de salida de ri_pgn. Mostró los nombres de sus
   archivos, entre ellos algunos que el cegamiento reserva. No abrí ninguno y no reporto de ellos nada más que lo que da `resumen_t2.py`.
   Lo declaro para que la autora decida si importa para U-MED-VERIF. Tendría que haber listado solo con un script que filtre los nombres.

## 9. Para la autora

1. **Cómo sigue la tanda** (§4.2), con estas opciones:
   - relanzar con el mismo tope: probablemente frena otra vez al cerrar ceninf:e1, si la razón no baja;
   - revisar el tope o el estimado;
   - otra cosa que decida.
   El relanzamiento es suyo, desde su terminal y con el mismo comando. Yo no relanzo.
2. **La doble cuenta de la fase que cierra** en la proyección (sección 5). Es una observación sobre el código sellado, que no toqué.
3. **`logs/cache_usage.jsonl`.** Cambia con la corrida y no está en la lista del «seguí» (sección 7).

FRENO T2 (parcial). Espero la revisión de la autora.
