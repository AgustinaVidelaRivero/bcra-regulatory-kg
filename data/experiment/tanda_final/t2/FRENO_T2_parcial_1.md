# FRENO T2 parcial 1 — tanda final de B6.1: el tramo 1 completo y el control entre tramos en FRENO (19/10/2026)

Pre-registro FIRMADO: `docs/preregistro_tanda_final.md` (firma en `4de7f2a7`), con su nota posterior a la firma (`27bfaeb5`), su versión
derivada de T1 y lo que del pre-registro de la tanda 1 no reemplaza. Rigen el §2, el §3, el §4.2, el §5 y el §8. Las decisiones de la
autora antes de la extracción están en el registro de decisiones, §42. HEAD `27bfaeb5`, al empezar y al terminar.

**Resultado:** lancé T2 una vez, a las 00:08:43, desde mi sesión. El lanzador corrió los 30 TOs del tramo 1, todos con salida 0 y con el
freno por modelo en OK, y paró a las 02:35:20 con **salida 11: el control entre tramos dio FRENO** en un criterio, los errores
definitivos (1, con umbral 0). Los otros tres criterios dieron OK. El tramo 2 no arrancó. **Gasto: USD 12,856189 de un tope de
151,5835.** Decide la autora. Seguir con el tramo 2 va con `--autorizado-tramo-2` y solo con su decisión por escrito; el lanzador no lo
relanza nadie más que ella desde su terminal.

**Las cifras:** salen de `freno_t2_cifras.py` → `freno_t2_cifras.md` (tablas 1 a 8) y `freno_t2_cifras.json`; la salida de `resumen_t2.py`,
de `resumen_t2_tramo1.txt` (y `.json`); la de `conteos_t2.py`, de `conteos_t2_tramo1.txt`. Desde la raíz del repo:
`python3 -I -B data/experiment/tanda_final/t2/freno_t2_cifras.py --repo "$PWD" --resumen data/experiment/tanda_final/t2/resumen_t2_tramo1.json --log data/experiment/tanda_final/t2/lanzador_T2_lanzamiento_1.log --foto-antes <json> --foto-despues <json> --comparacion <json> --md <md> --json <json>`
(las fotos están en el paquete).

## 0. Paso 0 (19/10/2026, 00:07:20 a 00:08:15)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git log -3 --format='%h %s'
27bfaeb5 Tanda final: el estimado de la extraccion repartido entre sus documentos por caracteres, con el mismo total y el mismo tope
5052364f Tanda final: la corrida en seco, la segmentacion de sus noventa y ocho documentos y el manifiesto de la extraccion
5d8cb917 Pre-registro de la tanda final: la revision entre tandas y la version derivada con los huecos de antes de la primera etapa
$ git status --porcelain --untracked-files=no
$ shasum -a 256 data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json
e9993b9dc87e866850a0357572f03c54a3b08dd56f5cb272e42da5d33c81dfeb  data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json
$ grep -n '^MANIFIESTO_SHA256' data/experiment/tanda_final/t2/lanzar_t2.py
90:MANIFIESTO_SHA256 = "e9993b9dc87e866850a0357572f03c54a3b08dd56f5cb272e42da5d33c81dfeb"
$ shasum -a 256 -c data/experiment/tanda_final/t1/sha256_para_T2.txt   (contados: OK y otros)
ok=499 otros=0
$ shasum -a 256 data/experiment/tanda_final/t1/sha256_para_T2.txt
12f7e21716108deae98fdba4408baaa7ec405632c13c33c353a35df8fd1a35e2  data/experiment/tanda_final/t1/sha256_para_T2.txt
$ pgrep -fl "runner_corpus.py|lanzar_t2.py"; echo "pgrep_rc=$?"
pgrep_rc=1
$ ls -d data/experiment/reextraccion_v2/corpus_tanda_final data/experiment/tanda_final/t2/avance_t2.jsonl "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda_final/lanzamiento_1"
  (los tres: No such file or directory)
$ pmset -g ps | head -1
Now drawing from 'AC Power'
$ ioreg -r -k AppleClamshellState -d 4 | grep '"AppleClamshellState"'
  |   "AppleClamshellState" = No
```

- **La consulta de deprecaciones** (00:07:42 a 00:07:43; `t2/consulta_deprecaciones_t2.txt`), con WebFetch y sin iniciar sesión, sin
  error: `claude-haiku-4-5-20251001` y `claude-sonnet-5`, «Active», sin fecha de deprecación, con los retiros tentativos «Not sooner
  than October 15, 2026» y «Not sooner than June 30, 2027»; ningún aviso para los dos en el historial; el aviso, «at least 60 days'
  notice». Sin cambios contra la consulta de T1. No hay retiro anunciado: no corresponde el freno del §4.2.
- **El registro de decisiones, §42** (en `27bfaeb5`), dice que lanza la ejecutora, desde su sesión. Trae además «la prueba del
  acumulado de las tandas 0 y 1 con el tramo 1», que el «seguí» no menciona: por indicación de la autora después del lanzamiento, la
  hace la mesa aparte, sobre una copia, cuando el control entre tramos dé OK. No la corrí. Este control dio FRENO.
- **La foto del repo antes** (00:08:03 a 00:08:15, `foto_repo_tanda_final_t1.py`): 53.296 entradas, 40 sin abrir y 342 enlaces. Los
  `.pyc` y `__pycache__`: 11.236 líneas.
- El piso de 30 GB y las 78 rutas los controló el lanzador (sección 1).

## 1. El lanzamiento (tabla 1)

Desde la raíz del repo, en segundo plano con `run_in_background`, una sola vez y sin ninguna opción de prueba ni de decisión:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda_final/t2/lanzar_t2.py --trabajo "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda_final/lanzamiento_1"
```

(con la salida de pantalla del lanzador a un archivo del scratchpad, que copié a `t2/lanzador_T2_lanzamiento_1.log`, y su código de
salida al final; `.gitignore:47` ignora los `.log`, y va en el paquete).

| # | inicio | pid | fin | minutos | copia de trabajo borrada | salida | parada |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19T00:08:43-0300 | 39763 | 2026-10-19T02:35:20-0300 | 146.6 | True | rc=11 | FRENO del control entre tramos: decide la autora |

Controles previos: ok=True; 161552636 KB libres; HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 del manifiesto True; tope True; tramos True. Freno por modelo antes del primer TO, sobre 98 TOs: OK (ids de E1 [], de E3 []).

- **Inicio** 00:08:43, **fin** 02:35:20 (146,6 min), **pid** 39763 (el del primer renglón de `avance_t2.jsonl`), **salida 11**. El último
  renglón de `avance_t2.jsonl` es `{"evento": "fin_lanzador", "ts": "2026-10-19T02:35:20-0300", "copia_de_trabajo_borrada": true}`: el
  lanzador terminó solo y **borró la copia de trabajo**. No quedó ningún proceso (`pgrep`, rc 1).

## 2. El control entre tramos (tabla 3)

Corrió al cerrar el tramo 1, sobre la copia del lanzador (`control_en_la_copia_igual: true`, el control sellado `ca5f9b7b…`), y dio
**FRENO**, con salida 3: **errores definitivos 1, con umbral 0**. Los otros tres dieron OK: el costo por unidad, 0,021391 (umbral
0,03423); las salidas inválidas de E1, 1 de 601, 0,001664 (umbral 0,01); la proporción a la cola, 13 de 601, 0,021631 (umbral 0,030109).
Información, sin umbral: 6 de 601 unidades con reintento por forma de E1. Su JSON (`t2/control_entre_tramos_tanda_final.json`):

```json
{
 "medido": {
  "tos": 30,
  "fases_cerradas": true,
  "unidades": 601,
  "gasto_usd": 12.856189,
  "errores": 1,
  "cola": 13,
  "salidas_invalidas_e1": 1,
  "reintento_por_forma_e1_informacion": 6
 },
 "criterios": [
  [
   "costo por unidad",
   0.021391,
   0.03423,
   "OK"
  ],
  [
   "salidas inválidas de E1",
   0.001664,
   0.01,
   "OK"
  ],
  [
   "errores definitivos",
   1,
   0,
   "FRENO"
  ],
  [
   "proporción a la cola",
   0.021631,
   0.030109,
   "OK"
  ]
 ]
}
```

## 3. Por TO, del registro de avance (tabla 2)

| TO | tramo | inicio | fin | min | rc | freno | ids E1 | ids E3 | gasto global USD |
|---|---|---|---|---|---|---|---|---|---|
| ri_bdp | 1 | 00:08:45 | 00:09:28 | 0.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.116308 |
| ri_ieccm | 1 | 00:09:28 | 00:10:21 | 0.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.173944 |
| ri_rcl | 1 | 00:10:21 | 00:11:18 | 0.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.247938 |
| ri_esd | 1 | 00:11:18 | 00:12:18 | 1.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.337087 |
| verac | 1 | 00:12:18 | 00:13:35 | 1.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.44331 |
| ri_acsf | 1 | 00:13:35 | 00:14:35 | 1.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.536516 |
| ri_cr | 1 | 00:14:35 | 00:16:53 | 2.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.737993 |
| ri_tvf | 1 | 00:16:53 | 00:18:41 | 1.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.882586 |
| ribspc | 1 | 00:18:41 | 00:19:26 | 0.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.961476 |
| asomut | 1 | 00:19:26 | 00:20:54 | 1.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.097621 |
| micemp | 1 | 00:20:54 | 00:22:16 | 1.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.23278 |
| ri_psp | 1 | 00:22:16 | 00:26:25 | 4.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.592264 |
| ri_transpa | 1 | 00:26:25 | 00:33:09 | 6.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.073539 |
| ri_iesinap | 1 | 00:33:09 | 00:36:04 | 2.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.305139 |
| ri_msrl | 1 | 00:36:04 | 00:42:18 | 6.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.809107 |
| ri_iepsp | 1 | 00:42:18 | 00:48:52 | 6.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.237836 |
| ri_ai | 1 | 00:48:52 | 00:52:24 | 3.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.554533 |
| ri_pspapt | 1 | 00:52:24 | 00:54:56 | 2.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.838885 |
| ri_tsa | 1 | 00:54:56 | 01:05:58 | 11.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 4.599198 |
| ri_tar | 1 | 01:05:58 | 01:08:38 | 2.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 4.868301 |
| ri_laft | 1 | 01:08:38 | 01:16:35 | 8.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 5.579745 |
| ri_dsf | 1 | 01:16:35 | 01:27:04 | 10.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 6.385675 |
| ri_nge | 1 | 01:27:04 | 01:29:13 | 2.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 6.670367 |
| ri_ot | 1 | 01:29:13 | 01:33:05 | 3.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 7.079451 |
| consyr | 1 | 01:33:05 | 01:38:50 | 5.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 7.640025 |
| ri_secoexpo | 1 | 01:38:50 | 01:49:23 | 10.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 8.547851 |
| seggar | 1 | 01:49:23 | 02:01:12 | 11.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 9.4721 |
| ri_sef | 1 | 02:01:12 | 02:08:06 | 6.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 10.208213 |
| cedin | 1 | 02:08:06 | 02:21:30 | 13.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 11.457829 |
| ri_ii_31_12_19 | 1 | 02:21:30 | 02:35:20 | 13.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 12.856189 |

Los 30 con salida 0 y el freno por modelo en OK, con los ids `claude-haiku-4-5-20251001` (E1, con sus reintentos) y `claude-sonnet-5`
(E3). Los minutos van redondeados por TO: su suma da 146,7 y el lanzamiento, 146,6.

## 4. La salida de `resumen_t2.py`, completa

`<repo>/.venv/bin/python -B data/experiment/tanda_final/t2/resumen_t2.py --repo "$PWD" --out data/experiment/tanda_final/t2/resumen_t2_tramo1.json`,
con sus valores por defecto (la `--salida` y la consola de T2), rc 0. Los 68 del tramo 2 no corrieron: van con 0 aceptadas y sus
unidades sin destino.

```
TO          unid c/part  acept  cola  err s/dest idsrep  cob cobE0     gasto
ri_bdp         3      3      3     0    0      0      0    T     T    0.1163
ri_ieccm       4      4      4     0    0      0      0    T     T    0.0576
ri_rcl         4      4      4     0    0      0      0    T     T    0.0740
ri_esd         5      5      5     0    0      0      0    T     T    0.0891
verac          5      5      5     0    0      0      0    T     T    0.1062
ri_acsf        6      6      6     0    0      0      0    T     T    0.0932
ri_cr          6      6      6     0    0      0      0    T     T    0.2015
ri_tvf         6      6      6     0    0      0      0    T     T    0.1446
ribspc         7      7      7     0    0      0      0    T     T    0.0789
asomut         8      8      8     0    0      0      0    T     T    0.1361
micemp         8      8      8     0    0      0      0    T     T    0.1352
ri_psp         9      9      9     0    0      0      0    T     T    0.3595
ri_transpa    11     11     10     0    1      0      0    T     T    0.4813
ri_iesinap    12     12     12     0    0      0      0    T     T    0.2316
ri_msrl       12     12     10     2    0      0      0    T     T    0.5040
ri_iepsp      13     13     12     1    0      0      0    T     T    0.4287
ri_ai         15     15     15     0    0      0      0    T     T    0.3167
ri_pspapt     16     16     16     0    0      0      0    T     T    0.2844
ri_tsa        17     17     17     0    0      0      0    T     T    0.7603
ri_tar        18     18     17     1    0      0      0    T     T    0.2691
ri_laft       26     26     26     0    0      0      0    T     T    0.7114
ri_dsf        28     28     26     2    0      0      0    T     T    0.8059
ri_nge        30     30     30     0    0      0      0    T     T    0.2847
ri_ot         32     32     32     0    0      0      0    T     T    0.4091
consyr        34     34     32     2    0      0      0    T     T    0.5606
ri_secoexpo    35     35     34     1    0      0      0    T     T    0.9078
seggar        36     36     34     2    0      0      0    T     T    0.9242
ri_sef        38     38     38     0    0      0      0    T     T    0.7361
cedin         66     66     65     1    0      0      0    T     T    1.2496
ri_ii_31_12_19    91     91     90     1    0      0      0    T     T    1.3984
reqcac         3      3      0     0    0      3      0    F     T    0.0000
cateloc       11     11      0     0    0     11      0    F     T    0.0000
convca        12     12      0     0    0     12      0    F     T    0.0000
socgar        12     12      0     0    0     12      0    F     T    0.0000
horari        13     13      0     0    0     13      0    F     T    0.0000
osapsa        13     13      0     0    0     13      0    F     T    0.0000
snp_atm       16     16      0     0    0     16      0    F     T    0.0000
pognme        17     17      0     0    0     17      0    F     T    0.0000
evacre        19     19      0     0    0     19      0    F     T    0.0000
regpri        20     20      0     0    0     20      0    F     T    0.0000
cescar        21     21      0     0    0     21      0    F     T    0.0000
ctacor        21     21      0     0    0     21      0    F     T    0.0000
fgarcp        22     22      0     0    0     22      0    F     T    0.0000
pscpp         22     22      0     0    0     22      0    F     T    0.0000
secfin        22     22      0     0    0     22      0    F     T    0.0000
incuca        23     23      0     0    0     23      0    F     T    0.0000
venliq        23     23      0     0    0     23      0    F     T    0.0000
fclef         28     28      0     0    0     28      0    F     T    0.0000
lavdin        29     29      0     0    0     29      0    F     T    0.0000
rmrtsd        31     31      0     0    0     31      0    F     T    0.0000
ccbcra        32     32      0     0    0     32      0    F     T    0.0000
apnf          34     34      0     0    0     34      0    F     T    0.0000
traval        35     35      0     0    0     35      0    F     T    0.0000
disres        38     38      0     0    0     38      0    F     T    0.0000
relact        38     38      0     0    0     38      0    F     T    0.0000
coltit        39     39      0     0    0     39      0    F     T    0.0000
raapal        40     40      0     0    0     40      0    F     T    0.0000
servco        40     40      0     0    0     40      0    F     T    0.0000
retype        41     41      0     0    0     41      0    F     T    0.0000
fabcra        42     42      0     0    0     42      0    F     T    0.0000
ri2_ci        45     45      0     0    0     45      0    F     T    0.0000
icmecma       48     48      0     0    0     48      0    F     T    0.0000
pfmipyme      52     52      0     0    0     52      0    F     T    0.0000
prevmi        52     52      0     0    0     52      0    F     T    0.0000
fimipyme      55     55      0     0    0     55      0    F     T    0.0000
garopt        55     55      0     0    0     55      0    F     T    0.0000
actgar        60     60      0     0    0     60      0    F     T    0.0000
gescre        61     61      0     0    0     61      0    F     T    0.0000
snp_mep       62     62      0     0    0     62      0    F     T    0.0000
opecam        65     65      0     0    0     65      0    F     T    0.0000
ordcom        65     65      0     0    0     65      0    F     T    0.0000
gracre        67     67      0     0    0     67      0    F     T    0.0000
supcon        67     67      0     0    0     67      0    F     T    0.0000
cryl          68     68      0     0    0     68      0    F     T    0.0000
tasint        69     69      0     0    0     69      0    F     T    0.0000
snp_debin     71     71      0     0    0     71      0    F     T    0.0000
afiltr        72     72      0     0    0     72      0    F     T    0.0000
autenf        75     75      0     0    0     75      0    F     T    0.0000
rrci          77     77      0     0    0     77      0    F     T    0.0000
rmgcti        81     81      0     0    0     81      0    F     T    0.0000
repefe        87     87      0     0    0     87      0    F     T    0.0000
snp_psp       89     89      0     0    0     89      0    F     T    0.0000
jafip         91     91      0     0    0     91      0    F     T    0.0000
inspag        93     93      0     0    0     93      0    F     T    0.0000
graloc       100    100      0     0    0    100      0    F     T    0.0000
adfsp        101    101      0     0    0    101      0    F     T    0.0000
seguef       101    101      0     0    0    101      0    F     T    0.0000
garant       106    106      0     0    0    106      0    F     T    0.0000
snp_cec      122    122      0     0    0    122      0    F     T    0.0000
snp_spd      130    130      0     0    0    130      0    F     T    0.0000
snp_dd       131    131      0     0    0    131      0    F     T    0.0000
ratio        133    133      0     0    0    133      0    F     T    0.0000
ratiofn      133    133      0     0    0    133      0    F     T    0.0000
finsec       134    134      0     0    0    134      0    F     T    0.0000
snp_tr_nc    136    136      0     0    0    136      0    F     T    0.0000
pimf         165    165      0     0    0    165      0    F     T    0.0000
depinv       203    203      0     0    0    203      0    F     T    0.0000
ctavis       271    271      0     0    0    271      0    F     T    0.0000
total       4951   4951    587    13    1   4350      0
gasto global USD 12.8562 de un tope de USD 151.5835 (dentro del tope); TOs con las dos fases cerradas: 30
[ri_bdp] corrida completa: gasto global=USD 0.1163 | wall=0.7 min
[ri_ieccm] corrida completa: gasto global=USD 0.1739 | wall=0.9 min
[ri_rcl] corrida completa: gasto global=USD 0.2479 | wall=0.9 min
[ri_esd] corrida completa: gasto global=USD 0.3371 | wall=1.0 min
[verac] corrida completa: gasto global=USD 0.4433 | wall=1.3 min
[ri_acsf] corrida completa: gasto global=USD 0.5365 | wall=1.0 min
[ri_cr] corrida completa: gasto global=USD 0.7380 | wall=2.3 min
[ri_tvf] corrida completa: gasto global=USD 0.8826 | wall=1.8 min
[ribspc] corrida completa: gasto global=USD 0.9615 | wall=0.7 min
[asomut] corrida completa: gasto global=USD 1.0976 | wall=1.4 min
[micemp] corrida completa: gasto global=USD 1.2328 | wall=1.3 min
[ri_psp] corrida completa: gasto global=USD 1.5923 | wall=4.1 min
[ri_transpa] corrida completa: gasto global=USD 2.0735 | wall=6.7 min
[ri_iesinap] corrida completa: gasto global=USD 2.3051 | wall=2.9 min
[ri_msrl] corrida completa: gasto global=USD 2.8091 | wall=6.2 min
[ri_iepsp] corrida completa: gasto global=USD 3.2378 | wall=6.5 min
[ri_ai] corrida completa: gasto global=USD 3.5545 | wall=3.5 min
[ri_pspapt] corrida completa: gasto global=USD 3.8389 | wall=2.5 min
[ri_tsa] corrida completa: gasto global=USD 4.5992 | wall=11.0 min
[ri_tar] corrida completa: gasto global=USD 4.8683 | wall=2.6 min
[ri_laft] corrida completa: gasto global=USD 5.5797 | wall=7.9 min
[ri_dsf] corrida completa: gasto global=USD 6.3857 | wall=10.5 min
[ri_nge] corrida completa: gasto global=USD 6.6704 | wall=2.1 min
[ri_ot] corrida completa: gasto global=USD 7.0795 | wall=3.8 min
[consyr] corrida completa: gasto global=USD 7.6400 | wall=5.7 min
[ri_secoexpo] corrida completa: gasto global=USD 8.5479 | wall=10.5 min
[seggar] corrida completa: gasto global=USD 9.4721 | wall=11.8 min
[ri_sef] corrida completa: gasto global=USD 10.2082 | wall=6.9 min
[cedin] corrida completa: gasto global=USD 11.4578 | wall=13.4 min
[ri_ii_31_12_19] corrida completa: gasto global=USD 12.8562 | wall=13.8 min
```

- **El tramo 1:** 601 unidades (601 con partes), **587 aceptadas, 13 en la cola y 1 error definitivo**, 0 sin destino, 0 ids repetidos;
  cobertura completa y cobertura exacta de la E0 en los 30; las dos fases cerradas en los 30 (tabla 4).
- **El error definitivo es de ri_transpa** (11 unidades: 10 aceptadas y 1 error). `resumen_t2.py` no da la unidad ni el tipo de error, y
  el runner no dejó ninguna línea `FRENO:` ni `ERROR:` en su salida de pantalla: las 30 líneas que toma `resumen_t2.py` son las de
  «corrida completa». No abrí la salida del runner para buscarlo. Un dato de T1, solo para ubicarlo: en la corrida en seco, ri_transpa
  tenía una unidad que se partía por corte (`ri_transpa::Sbloque1::chapeau_seccion`, 21.712 caracteres; FRENO T1, sección 6), y acá
  ri_transpa no registra partes (11 con partes, igual que sus 11 unidades). Identificar la unidad y su error pide leer su
  `extracciones_e1.jsonl`; lo decide la autora.

## 5. `conteos_t2.py` y los `NO_ABRIR_`

`<repo>/.venv/bin/python -B data/experiment/tanda_final/t2/conteos_t2.py --repo "$PWD"`, con sus valores por defecto, rc 0
(`t2/conteos_t2_tramo1.txt`):

```
sha256 e3616d66483f4dd6167577ae356890d04d704d3382de621410ada8d2a1cf3c38
vigilancia integridad_e3: OK
```

Los dos `NO_ABRIR_`, que no abrí (solo su sha256):

```
d038a6460f5722c71e5f011b935de6bc73f1e2ad260eeeeaf40d20756d5c5942  data/experiment/tanda_final/t2/NO_ABRIR_salida_e3_tanda_final.txt
e3616d66483f4dd6167577ae356890d04d704d3382de621410ada8d2a1cf3c38  data/experiment/tanda_final/t2/NO_ABRIR_conteos_reextracciones_tanda_final.json
```

## 6. El costo y la duración (tablas 5, 6 y 7)

| cifra | valor |
|---|---|
| gasto real del tramo 1 (suma por TO, resumen_t2) | 12.856189 |
| gasto global (estado del runner) | 12.856189 |
| tramo 1, estimado del §3 (601 × 0,021115) | 12.6901 |
| tramo 1, líneas de alcance de A3 | 0.088479 |
| tramo 1, §3 más las líneas | 12.778594 |
| tramo 1, real / (§3 más las líneas) | 1.0061 |
| tramo 1, estimado repartido (manifiesto) | 19.310012 |
| tramo 1, real / repartido | 0.6658 |
| tramo 2, §3 más las líneas y repartido (sin correr) | 91.971209 y 85.439791 |
| total estimado (USD 104,7498) y gasto global / total | 104.749803 y 0.1227 |
| tope, gasto global / tope y margen | 151.5835, 0.0848 y 138.727311 |
| por TO, real / §3: mínimo y máximo | ['ri_nge', '0.4456'] y ['ri_tsa', '2.1007'] |
| por TO, real / repartido: mínimo y máximo | ['ri_psp', '0.2162'] y ['ri_nge', '4.0737'] |

- **El gasto real del tramo 1 es USD 12,856189**, 1,0061 veces el estimado del §3 más las líneas de alcance (12,6901 + 0,088479 =
  12,778594), y 0,6658 veces el repartido del manifiesto (19,310012). El reparto sobreestimó el tramo 1: la proyección del runner no
  frenó. Por TO (tabla 5), lo real va de 0,4456 a 2,1007 veces el estimado del §3 y de 0,2162 a 4,0737 veces el repartido.
- **Contra el tope:** 0,0848 del tope de USD 151,5835, con un margen de 138,727311. Contra el total estimado (USD 104,7498), 0,1227: el
  tramo 2 no corrió.
- **La duración:** 146,6 min el lanzamiento, contra 148,6 proyectados para el tramo 1 por unidades y 183,5 por caracteres. La tanda
  entera se proyectaba en 1.223,8 min por unidades y 995,5 por caracteres.

| cifra | valor |
|---|---|
| lanzamiento (inicio_lanzador a fin_lanzador, min) | [146.6] |
| suma de los TOs (to_inicio a to_fin, min) | 146.7 |
| tramo 1 proyectado por unidades y por caracteres (min) | 148.6 y 183.5 |
| la tanda proyectada por unidades y por caracteres (min) | 1223.8 y 995.5 |

## 7. La foto del repo, los commits, los `.pyc` y el grep (tabla 8)

- **La foto después** (02:36:23 a 02:36:35, el mismo script): 53.882 entradas, 42 sin abrir y 342 enlaces. Comparación: **586 nuevos, 0
  borrados y 4 cambiados.**
  - Los nuevos: 579 en `data/experiment/reextraccion_v2/corpus_tanda_final/` y 7 en `data/experiment/tanda_final/t2/` (los dos
    `NO_ABRIR_`, `avance_t2.jsonl`, `control_entre_tramos_tanda_final.json`, `resumen_t2_tramo1.json`, `resumen_t2_tramo1.txt` y
    `conteos_t2_tramo1.txt`). `consulta_deprecaciones_t2.txt` es anterior a la foto de antes, y este FRENO, el script de las cifras y
    sus salidas y el log del lanzador, posteriores a la de después.
  - Los cambiados: las tres bases de la caché y `logs/cache_usage.jsonl`. Van solo por su tamaño y su fecha (`stat`, a las 02:36):
    - `e1_extractor/cache/e1_extraccion.db`: 762.617.856 bytes, 02:31:49;
    - `e3_verificador/cache/e1_reintentos.db`: 77.680.640 bytes, 02:35:17;
    - `e3_verificador/cache/e3_verificacion.db`: 414.482.432 bytes, 02:35:17;
    - `logs/cache_usage.jsonl`: 5.737.617 bytes, 02:35:17.
    El script de la foto calcula el sha256 de esos cuatro archivos al leerlos, como en T1, sin mostrar su contenido; acá no lo doy.
  - **`data/experiment/neo4j/volumen/`:** sin cambios. Ninguna otra ruta cambió.
  - Los 40 sin abrir de antes, con el mismo tamaño y la misma fecha; los 2 nuevos son los `NO_ABRIR_` de `t2/`.
- **Los commits de la autora durante T2:** ninguno. `git log 27bfaeb5..HEAD` sale vacío, y HEAD sigue en `27bfaeb5`.
- **Los `.pyc`:** 11.236 líneas antes y 11.236 después, iguales (`diff` vacío).
- **El grep de convenciones:** sobre los 11 archivos nuevos de `t2/` que no son `NO_ABRIR_` (este FRENO, el script de las cifras y sus dos salidas, las dos de
  `resumen_t2.py`, la de `conteos_t2.py`, la consulta de deprecaciones, `avance_t2.jsonl`, el JSON del control y el log del lanzador).
  Los tokens del nombre salen de `git config user.name` en la consola y no quedan escritos en ningún archivo, más la lista de términos
  de la sección 11 del FRENO T1, con `grep -c -i -E`. **Ninguno con una cuenta distinta de 0, y ninguno con una ruta personal**
  (`/Users/` o `/private/tmp`). El control positivo da 1.
- **Lo que leyó la foto:** el script de la foto, el de T1 como pide el «seguí», recorre el repo entero y calcula el sha256 de cada
  archivo, así que leyó los archivos nuevos de la salida del runner y los cuatro de la caché, sin mostrar su contenido. Yo no listé
  ni abrí la salida: de la comparación tomé solo cuentas por carpeta (tabla 8). Las fotos enteras y su comparación nombran cada ruta
  del repo y de la salida, y no van al paquete: van su sha256 y sus conteos (`resumen_fotos_T2.json`).

## 8. Para la autora

1. **El FRENO del control entre tramos: 1 error definitivo en ri_transpa** (sección 4). Seguir con el tramo 2 va con
   `--autorizado-tramo-2` y su decisión por escrito; el relanzamiento es desde su terminal (registro, §42). Con el tramo 1 cerrado, el
   runner saltea sus fases y el control vuelve a correr y a quedar en el registro.
2. **El costo del tramo 1** quedó en 1,0061 veces el §3 más las líneas, y el reparto lo sobreestimó (0,6658). El gasto acumulado está
   lejos del tope y de los USD 341.
3. **La prueba del acumulado con el tramo 1** (§42) es de la mesa, cuando el control dé OK. Este dio FRENO.
4. **La pausa del viernes 23/10 a las 18:00** sigue en el lanzador: un relanzamiento después de esa hora va con `--retomar-tras-pausa`,
   solo con su decisión por escrito.

## 9. Errores propios, con su causa

1. **Un archivo en `/tmp`.** En el paso 0, un comando mandó la salida de `shasum -a 256 -c` a `/tmp/null_t2_check` y lo borró en el
   mismo comando, fuera del scratchpad. Causa: quise descartar esa salida antes de contarla, y la cuenta la saqué con otro `shasum -c`. No
   afectó ninguna cifra, y no quedó nada.

## 10. El paquete

`revision_tanda_final_FRENO_T2_parcial_1/`, en el scratchpad de la sesión (`afadde2e-6298-47fb-9777-7fcb43152d50`), con su `manifest.txt`
(sha256 y una línea por archivo). Lleva «parcial_1» en el nombre para no chocar con el paquete del FRENO T2 final. Su copia con `ditto`
está en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T2_parcial_1/`.
La verificación de la copia va en el mensaje del FRENO. No lleva los `NO_ABRIR_` ni nada de la salida del runner, ni las fotos enteras.

FRENO T2 parcial 1. Espero la decisión de la autora.
