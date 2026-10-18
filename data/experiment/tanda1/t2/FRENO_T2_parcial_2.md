# FRENO T2 (parcial 2) — tanda 1 de B6.1: el segundo lanzamiento frenó por proyección en ri_rml (17/10/2026, sin commit)

Rigen el §2, el §3, el §4.2 y el §7 del pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`). HEAD `ea61cfdb`.

**La decisión de la autora** (§4.2, tras revisar el parcial 1): relanzar T2 con el mismo tope (USD 100,7291) y el mismo comando, una sola
vez, desde esta sesión, porque una proyección con 2 TOs no alcanza para decidir el tope. No cambió el tope ni el estimado.

**El segundo lanzamiento salió con 3, otra vez un freno por proyección:**

```
FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21     (lanzamiento 1)
FRENO: proyección USD 122.79 supera el tope global USD 100.73 en ri_rml:e1 50/50     (lanzamiento 2)
```

- **Lo que se hizo:** ri_gerc, ri_pgn y ceninf completos; ri_rml con su E1 cerrada y su E3 sin empezar. Los otros 16 TOs no empezaron.
- **El gasto:** USD 3,664724 de un tope de 100,7291.
- **Lo que no hice:** no relancé y no subí el tope. Decide la autora (§4.2).
- **El parcial 1 no se pisó:** lo renombré a `FRENO_T2_parcial_1.md` sin cambiarle el contenido (sha256 `49e2dca8…` antes y después).
  Allí está el paso 0 del «seguí» y el detalle del lanzamiento 1.
- Nada commiteado y ningún mensaje de commit preparado: el commit es de la autora y queda PENDIENTE.

## 1. Los controles antes del lanzamiento 2 (16/10/2026, 23:33:43)

```
$ git log -1 --format=%h
ea61cfdb
$ git status --porcelain --untracked-files=no
$ pgrep -fl "runner_corpus.py|lanzar_t2.py"
(rc=1)
$ tail -1 data/experiment/tanda1/t2/avance_t2.jsonl
{"evento": "fin_lanzador", "ts": "2026-10-16T21:01:43-0300", "copia_de_las_bases_borrada": true}
no existe: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_2
```

- `git status` y `pgrep` salieron vacíos.
- `df -k .`: 186.677.224 KB libres.
- **La foto antes del lanzamiento 2** (`t2/foto_repo_tanda1_t2.py`, de 23:34:01 a 23:34:11): 51.232 entradas. Los `.pyc`: 11.236 líneas.

## 2. El lanzamiento 2

Desde la raíz del repo, en segundo plano (`run_in_background`), una sola vez, sin `--stub`, `--solo-tos` ni `--git-repo`:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_2"
```

- **Inicio:** 16/10/2026 23:34:21 (`inicio_lanzador`, pid 25724). **Fin:** 17/10/2026 00:17:08 (`fin_lanzador`). Duró 42,8 min.
- **Código de salida: 3** (la app avisó «exited with code 3»).
- **`controles_previos`** (23:34:22), todo OK:
  - el piso: 186.669.368 KB libres, contra 31.457.280;
  - las rutas: `HEAD:  78 de 78`, `árbol: 78 de 78`;
  - el SDK: `0.100.0`;
  - el sha256 y el tope del manifiesto;
  - la carpeta de trabajo, fuera del repo y nueva.
- **`freno_modelo_antes`** (23:34:23): OK, con E1 `claude-haiku-4-5-20251001` y E3 `claude-sonnet-5`, que son las filas del lanzamiento 1.
- **El cierre:** el último renglón es `{"evento": "fin_lanzador", "ts": "2026-10-17T00:17:08-0300", "copia_de_las_bases_borrada": true}`.
  Lo precede la `parada` «el runner salió con 3 en ri_rml» (00:17:08).
- **La copia de trabajo de las bases:** borrada (`ls` de `bases_lanzamiento_2`: «No such file or directory»).

**Por TO, los renglones de los dos lanzamientos** (`avance_t2.jsonl`, sha256 `fa239f4f…`):

| lanz. | TO | inicio | fin | min | rc | freno por modelo | ids de E1 | ids de E3 | gasto global USD |
|---:|---|---|---|---:|---:|---|---|---|---:|
| 1 | ri_gerc | 20:48:15 | 20:51:33 | 3,3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0,352899 |
| 1 | ri_pgn | 20:51:33 | 21:01:43 | 10,2 | 3 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ri_gerc | 23:34:23 | 23:34:24 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ri_pgn | 23:34:24 | 23:34:26 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ceninf | 23:34:26 | 23:42:17 | 7,8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,957244 |
| 2 | ri_rml | 23:42:17 | 00:17:08 | 34,9 | 3 | OK | claude-haiku-4-5-20251001 | (vacío) | 3,664724 |

- **En el lanzamiento 2, ri_gerc y ri_pgn** tenían sus fases cerradas: el runner las salteó y corrió solo su E2, que es offline. El de ri_pgn
  corrió por primera vez. El gasto no cambió.
- **En ri_rml, el conjunto de ids de E3 sale vacío** porque su E3 no empezó.

## 3. La salida de `resumen_t2.py`, completa

`.venv/bin/python -B data/experiment/tanda1/t2/resumen_t2.py --repo . --out data/experiment/tanda1/t2/resumen_t2.json` (rc 0;
`resumen_t2.json`, sha256 `a5ecf599…`):

```
TO          unid c/part  acept  cola  err s/dest idsrep  cob cobE0     gasto
ri_gerc       15     15     15     0    0      0      0    T     T    0.3529
ri_pgn        21     21     20     1    0      0      0    T     T    0.7962
ceninf        39     39     39     0    0      0      0    T     T    0.8082
ri_rml        46     50      0     0    0     50      0    F     T    1.7075
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
total       3290   3294     74     1    0   3219      0
gasto global USD 3.6647 de un tope de USD 100.7291 (dentro del tope); TOs con las dos fases cerradas: 3
[ri_gerc] corrida completa: gasto global=USD 0.3529 | wall=3.3 min
[ri_pgn] FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21
[ri_gerc] corrida completa: gasto global=USD 1.1491 | wall=0.0 min
[ri_pgn] corrida completa: gasto global=USD 1.1491 | wall=0.0 min
[ceninf] corrida completa: gasto global=USD 1.9572 | wall=7.8 min
[ri_rml] FRENO: proyección USD 122.79 supera el tope global USD 100.73 en ri_rml:e1 50/50
```

- **En los tres TOs completos:** 75 unidades, 74 aceptadas, 1 en cola (de ri_pgn) y 0 errores; cobertura completa, 0 ids repetidos y la
  cobertura exacta de la E0.
- **En ri_rml:** 50 unidades con partes. Son sus 46, y `ri_rml::Sbloque14` se partió en 5, como había previsto la corrida en seco
  (`tanda1/t1/seco/censo_unidades_grandes_t1.json`). Tienen E1 pero no E3: por eso salen «sin destino».

## 4. La salida de `conteos_t2.py` y los `NO_ABRIR_`

`.venv/bin/python -B data/experiment/tanda1/t2/conteos_t2.py --repo .` (rc 0):

```
sha256 0cc14825bb5a2cc93675f414bcec7701f8f546aa394393d44aaf9a2a94b77d45
vigilancia integridad_e3: OK
```

El sha256 de los dos `NO_ABRIR_`, que no abrí:

```
0dcb082bedb976d769d253e0234e8b73f160facf8672b9490fe0da0a0044f4fe  data/experiment/tanda1/t2/NO_ABRIR_salida_e3_tanda1.txt
0cc14825bb5a2cc93675f414bcec7701f8f546aa394393d44aaf9a2a94b77d45  data/experiment/tanda1/t2/NO_ABRIR_conteos_reextracciones_tanda1.json
```

## 5. El gasto por TO contra su estimado y la proyección reproducida

**Por TO** (los gastos de `estado_corpus.json`, `fases_cerradas`; el estimado, del manifiesto):

| TO | fases cerradas | real USD | estimado USD | razón |
|---|---|---:|---:|---:|
| ri_gerc | e1, e3 | 0,352899 | 0,319465 | 1,1047 |
| ri_pgn | e1, e3 | 0,796164 | 0,447252 | 1,7801 |
| ceninf | e1, e3 | 0,808181 | 0,823485 | 0,9814 |
| ri_rml | solo e1 | 1,707480 | 0,474614 (su e1) | 3,5976 |
| **lo pagado** | 7 fases | **3,664724** | **2,064816** | **1,7748** |

- ri_rml tiene la unidad más grande de la tanda: `ri_rml::Sbloque14`, de 50.404 caracteres, partida en 5, con tres de sus partes en el tercer
  escalón según la corrida en seco.
- En la corrida en seco, ri_rml era el TO con más pedidos que cortan con la salida p90: 16, con una cota de salida de USD 0,8192
  (`tanda1/t1/seco/estimado_por_to_t1.json`).
- No leí nada de la salida de E1 de ri_rml que diga cuánto de su gasto fue de cortes o del tercer escalón. Eso no está en lo que el «seguí»
  pide reportar.

**La proyección** (`runner_corpus.py:400-430`, en el checkpoint de cierre de ri_rml:e1, `:433-451`, llamado en `:837`):

| | USD |
|---|---:|
| gasto real (las 7 fases cerradas) | 3,664724 |
| estimado de esas 7 fases | 2,064816 |
| razón = factor | 1,7748 |
| estimado total del runner | 69,659 |
| estimado corrido, con ri_rml:e1 contada dos veces (como en el parcial 1) | 2,539430 |
| estimado restante | 67,119570 |
| **proyección** = 3,664724 + 1,7748 × 67,119570 | **122,7914** |
| tope | 100,7291 |

- Sin la doble cuenta de la fase que cierra, la proyección da 123,6338.
- Con los números de hoy, frena una razón de más de (100,7291 − 3,664724) / 67,119570 = 1,4461.

**El estado en disco** (`estado_corpus.json`):
- las 7 fases cerradas: ri_gerc:e1, ri_gerc:e3, ri_pgn:e1, ri_pgn:e3, ceninf:e1, ceninf:e3 y ri_rml:e1;
- `fase_actual` en null.

**Qué haría un tercer lanzamiento con el mismo tope.** Esto es lectura del código, no lo corrí:
- saltea las 7 fases cerradas;
- corre otra vez los E2 de los tres TOs completos;
- hace el E3 de ri_rml entero, porque el margen antes de cada unidad pasa;
- vuelve a proyectar al cerrar ri_rml:e3, y después al cerrar cada fase de nmcief;
- y frena mientras la razón de lo pagado pase alrededor de 1,45.

## 6. Gasto y duración contra lo proyectado

- **Gasto:** USD 3,664724 en 3 TOs completos y la E1 de un cuarto. Pasaron por E1 121 de las 3.290 unidades de la E0 (15 + 21 + 39 + 46),
  125 con las partes de ri_rml.
  - Contra el estimado de lo pagado (2,064816), es 1,7748 veces.
  - Contra el estimado de la tanda (69,6592), es el 5,26 %; contra el tope (100,7291), el 3,64 %.
- **Duración:**
  - **Trabajo nuevo:** 13,5 min en el lanzamiento 1 y 42,7 min en el 2 (ceninf 7,8 y ri_rml 34,9).
  - **ceninf:** 39 unidades en 7,8 min, unos 12,1 s por unidad, cerca de los 11,84 de la tanda 0.
  - **ri_rml:** su E1 sola tardó 34,9 min con 50 unidades.
  - **Contra los ~649 min proyectados:** con 4 de 20 TOs no se puede corregir esa proyección.

## 7. La foto del repo, los .pyc y el grep de convenciones

- **Del lanzamiento 2** (`foto_repo_tanda1_t2.py`). Antes: 23:34:01 a 23:34:11, 51.232 entradas. Después: 17/10 00:18:36 a 00:18:47, 51.266
  entradas.
  - **35 nuevos:** 34 en `reextraccion_v2/corpus_tanda1/` y `t2/FRENO_T2_parcial_1.md`, que es el renombre.
  - **1 borrado:** `t2/FRENO_T2.md` (el parcial 1, renombrado).
  - **11 cambiados:**
    - `estado_corpus.json`, `presupuesto_compartido.json` y `ultimo_checkpoint.json` de la salida;
    - las tres bases del runner, solo por tamaño y fecha: `e1_extraccion.db` de 410.034.176 a 419.590.144 bytes, `e1_reintentos.db` de
      54.325.248 a 54.415.360 y `e3_verificacion.db` de 267.808.768 a 269.209.600;
    - en `t2/`, `avance_t2.jsonl`, `resumen_t2.json` y los dos `NO_ABRIR_`;
    - `logs/cache_usage.jsonl`, solo por tamaño y fecha: de 3.929.020 a 3.959.624.
  - Nada fuera de esas rutas.
- **Desde el inicio de T2** (contra la foto de las 20:47:34): 70 nuevos (65 en `corpus_tanda1/` y 5 en `t2/`), 2 borrados (el `-shm` y el
  `-wal` de `e1_extraccion.db`) y 4 cambiados (las tres bases y `logs/cache_usage.jsonl`).
  - **En `t2/`, además, respecto de HEAD:** `foto_repo_tanda1_t2.py`, escrito antes de la primera foto, y este FRENO, escrito después de la
    última.
  - **`logs/cache_usage.jsonl`** sigue fuera de la lista de lo nuevo del «seguí» (parcial 1, sección 9, punto 3).
- `git status --porcelain --untracked-files=no` sigue vacío.
- **Los `.pyc`:** 11.236 al inicio de T2 y 11.236 después del lanzamiento 2, iguales (`diff` vacío).
- **El grep de convenciones** sobre lo nuevo de `t2/`, sin los `NO_ABRIR_`. El resultado, con el control positivo, va en el mensaje del FRENO.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. No hice ninguna copia del repo.
- **Lo que miré en disco:**
  - durante la corrida, solo `avance_t2.jsonl`;
  - después, solo las fotos, que dejan las bases y el log de uso por tamaño, y `estado_corpus.json`, del que usé solo los gastos y los
    nombres de las fases cerradas.
  - Ningún `ls` de las carpetas de salida.

## 8. Errores propios

Ninguno en este lanzamiento. Los dos del parcial 1 siguen declarados allí.

## 9. Para la autora

1. **Cómo sigue la tanda** (§4.2). La razón de lo pagado subió de 1,4987 a 1,7748. ceninf costó lo estimado (0,98 veces), y los dos
   regímenes informativos que más cuestan son ri_pgn (1,78 veces) y la E1 de ri_rml (3,60 veces). Un tercer lanzamiento con el mismo tope
   haría el E3 de ri_rml y volvería a proyectar al cerrarlo (sección 5).
2. **La doble cuenta de la fase que cierra** en la proyección sigue igual (parcial 1, sección 5). Acá baja la proyección en 0,84.

FRENO T2 (parcial 2). Espero la revisión de la autora.
