# FRENO T2 — tanda final de B6.1: la extracción E1 a E3 de los 98 TOs, en dos lanzamientos (19 y 20/10/2026)

Pre-registro FIRMADO: `docs/preregistro_tanda_final.md` (firma en `4de7f2a7`), con su nota posterior a la firma (`27bfaeb5`), su versión
derivada de T1 y lo que del pre-registro de la tanda 1 no reemplaza. Rigen el §2, el §3, el §4.2, el §5 y el §8; las decisiones de la
autora, en el registro de decisiones, §42. HEAD al lanzar: `27bfaeb5`; al terminar: `729dc565`, con 12 commits de la autora en el medio
(sección 8). Lo anterior a este FRENO: el FRENO T2 parcial 1 (`t2/FRENO_T2_parcial_1.md`), la identificación del error
(`t2/identificacion_error_ri_transpa/`) y la decisión de la autora de seguir (sección 2).

**Resultado: los 98 TOs completos.** El lanzamiento 1 (19/10, 00:08:43 a 02:35:20) corrió el tramo 1 y paró con salida 11: el control
entre tramos dio FRENO por 1 error definitivo. Con la decisión de la autora por escrito, el lanzamiento 2 (19/10, 08:42:24, a 20/10,
00:11:16, con `--autorizado-tramo-2`) volvió a pasar el control (FRENO, en el registro), siguió con los 68 del tramo 2 y terminó con
**salida 0**. Los 98, con salida 0 y el freno por modelo en OK (`claude-haiku-4-5-20251001` en E1 y `claude-sonnet-5` en E3).
**4.951 unidades: 4.870 aceptadas, 80 en la cola y 1 error definitivo** (`ri_transpa::Sbloque1::chapeau_seccion`, de E1), 0 sin destino
y 0 ids repetidos. **Gasto: USD 97,598343, 0,9317 del estimado (104,749803) y 0,6439 del tope (151,5835).** Duración: 1.075,5 min entre
los dos lanzamientos, contra 1.223,8 proyectados por unidades y 995,5 por caracteres. Nada commiteado; los commits son de la autora.

**Las cifras:** salen de `freno_t2_final_cifras.py` → `freno_t2_final_cifras.md` (tablas 1 a 8b) y `.json`; la salida de `resumen_t2.py`,
de `resumen_t2_final.txt` (y `.json`); la de `conteos_t2.py`, de `conteos_t2_final.txt`. Desde la raíz del repo:
`python3 -I -B data/experiment/tanda_final/t2/freno_t2_final_cifras.py --repo "$PWD" --resumen data/experiment/tanda_final/t2/resumen_t2_final.json --log data/experiment/tanda_final/t2/lanzador_T2_lanzamiento_1.log --log data/experiment/tanda_final/t2/lanzador_T2_lanzamiento_2.log --foto-antes <json> --foto-despues <json> --comparacion <json> --head-antes 27bfaeb5 --md <md> --json <json>`
(los dos `.log` los ignora `.gitignore:47`; van en el paquete, como el resumen de las fotos). El script del FRENO parcial 1
(`freno_t2_cifras.py`) y sus salidas quedan como estaban.

## 0. El paso 0 (19/10/2026, 00:07:20 a 00:08:15) y los controles del lanzamiento 2 (08:42:10)

El paso 0 completo, con su salida, está en el FRENO T2 parcial 1, sección 0. En resumen:
- `main`; `git log -3`: `27bfaeb5` (el estimado repartido) y `5052364f` (la corrida en seco), en ese orden; `git status --porcelain
  --untracked-files=no` vacío; `pgrep` con rc 1;
- el manifiesto, `e9993b9dc87e866850a0357572f03c54a3b08dd56f5cb272e42da5d33c81dfeb`, el mismo valor que `MANIFIESTO_SHA256` del
  lanzador (renglón 90); `shasum -a 256 -c data/experiment/tanda_final/t1/sha256_para_T2.txt`: **499 `OK` y ninguno distinto**; la
  lista, `12f7e21716108deae98fdba4408baaa7ec405632c13c33c353a35df8fd1a35e2`;
- no existían `corpus_tanda_final/`, `t2/avance_t2.jsonl` ni la carpeta de trabajo del lanzamiento 1;
- la Mac: «Now drawing from 'AC Power'» y `"AppleClamshellState" = No`;
- **la consulta de deprecaciones** (00:07:42 a 00:07:43; `t2/consulta_deprecaciones_t2.txt`), con WebFetch y sin iniciar sesión, sin
  error: los dos modelos «Active», sin fecha de deprecación, con los retiros tentativos «Not sooner than October 15, 2026» y «Not sooner
  than June 30, 2027», ningún aviso para ellos y el aviso de «at least 60 days' notice». Sin cambios: no corresponde el freno del §4.2;
- la foto del repo antes (00:08:03 a 00:08:15): 53.296 entradas, 40 sin abrir y 342 enlaces; los `.pyc`, 11.236.

Antes del lanzamiento 2 (08:42:10): `git status --porcelain --untracked-files=no` vacío y HEAD en `27bfaeb5`; `pgrep` con rc 1; el
manifiesto, `e9993b9d…`; «AC Power» y `"AppleClamshellState" = No`; la carpeta del lanzamiento 2 no existía.

## 1. Los lanzamientos (tabla 1)

Desde la raíz del repo, en segundo plano con `run_in_background`, cada uno una sola vez:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda_final/t2/lanzar_t2.py --trabajo "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda_final/lanzamiento_1"
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda_final/t2/lanzar_t2.py --autorizado-tramo-2 --trabajo "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda_final/lanzamiento_2"
```

(la salida de pantalla de cada uno, a un archivo del scratchpad copiado a `t2/lanzador_T2_lanzamiento_<n>.log`, con su código de salida
al final). Ninguno llevó `--stub`, `--solo-tos-*`, `--git-repo`, `--hora-simulada` ni `--retomar-tras-pausa`.

| # | inicio | pid | fin | minutos | salida | opciones | controles previos | freno antes | parada | copia de trabajo borrada |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19T00:08:43-0300 | 39763 | 2026-10-19T02:35:20-0300 | 146.6 | rc=11 | autorizado_tramo_2=False, retomar_tras_pausa=False, stub=False | True (HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 True; tope True) | OK [] [] | FRENO del control entre tramos: decide la autora | True |
| 2 | 2026-10-19T08:42:24-0300 | 70654 | 2026-10-20T00:11:16-0300 | 928.9 | rc=0 | autorizado_tramo_2=True, retomar_tras_pausa=False, stub=False | True (HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 True; tope True) | OK ['claude-haiku-4-5-20251001'] ['claude-sonnet-5'] | — | True |

- El último renglón de `avance_t2.jsonl`: `{"evento": "fin_lanzador", "ts": "2026-10-20T00:11:16-0300", "copia_de_trabajo_borrada": true}`.
  **Las dos copias de trabajo quedaron borradas.** No quedó ningún proceso.

## 2. El FRENO T2 parcial 1, la identificación y la decisión

- **El FRENO T2 parcial 1** (`t2/FRENO_T2_parcial_1.md`, sha256 `6427730f…`): el tramo 1 completo, con USD 12,856189, y el control
  entre tramos en FRENO por 1 error definitivo en ri_transpa.
- **La identificación** (`t2/identificacion_error_ri_transpa/`, con su FRENO corto, `097a3940…`): el error es de E1, en
  `ri_transpa::Sbloque1::chapeau_seccion` (`mini_chunk`, 21.712 caracteres), `salida_mal_formada_tras_reintento`. El primer intento (8.192)
  terminó con `tool_use` y 6.132 tokens, mal formado; los dos reintentos por forma, a temperatura 1 y con el mismo 8.192, cortaron. El
  reintento por forma no escala el max_tokens ni parte la unidad. 25 unidades del tramo 2 estaban expuestas a ese camino.
- **La decisión de la autora, por escrito** (19/10/2026): seguir con el tramo 2 con `--autorizado-tramo-2`; el error es de esa unidad (el
  reintento por forma no escala el max_tokens, `runner_corpus.py:683-685`); no se toca el código; la unidad se trata después del tramo 2,
  con un mandato aparte, y queda declarada. Relanzé yo, desde mi sesión, como el lanzamiento 1.
- **En el tramo 2 no falló ninguna unidad:** 0 errores en sus 68 TOs (sección 5), tampoco en las 25 expuestas.

## 3. Los controles entre tramos (tabla 3)

| lanz. | hora | rc | resultado | salida | control sha256 |
|---|---|---|---|---|---|
| 1 | 2026-10-19T02:35:20-0300 | 3 | FRENO | OK    costo por unidad: 0.021391 (umbral 0.03423) / OK    salidas inválidas de E1: 0.001664 (umbral 0.01) / FRENO errores definitivos: 1 (umbral 0) / OK    proporción a la cola: 0.021631 (umbral 0.030109) / info  reintento por forma de E1: 6 de 601 unidades (sin umbral) | ca5f9b7bb363… |
| 2 | 2026-10-19T08:43:31-0300 | 3 | FRENO | OK    costo por unidad: 0.021391 (umbral 0.03423) / OK    salidas inválidas de E1: 0.001664 (umbral 0.01) / FRENO errores definitivos: 1 (umbral 0) / OK    proporción a la cola: 0.021631 (umbral 0.030109) / info  reintento por forma de E1: 6 de 601 unidades (sin umbral) | ca5f9b7bb363… |

Los dos dieron lo mismo: FRENO en errores definitivos (1, umbral 0) y OK en los otros tres. El del lanzamiento 2 quedó en el registro y
el lanzador siguió por `--autorizado-tramo-2`. El JSON (`t2/control_entre_tramos_tanda_final.json`, el del lanzamiento 2):

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

## 4. Por TO, del registro de avance (tabla 2)

| lanz. | TO | tramo | inicio | fin | min | rc | freno | ids E1 | ids E3 | gasto global USD |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ri_bdp | 1 | 2026-10-19 00:08:45 | 00:09:28 | 0.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.116308 |
| 1 | ri_ieccm | 1 | 2026-10-19 00:09:28 | 00:10:21 | 0.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.173944 |
| 1 | ri_rcl | 1 | 2026-10-19 00:10:21 | 00:11:18 | 0.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.247938 |
| 1 | ri_esd | 1 | 2026-10-19 00:11:18 | 00:12:18 | 1.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.337087 |
| 1 | verac | 1 | 2026-10-19 00:12:18 | 00:13:35 | 1.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.44331 |
| 1 | ri_acsf | 1 | 2026-10-19 00:13:35 | 00:14:35 | 1.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.536516 |
| 1 | ri_cr | 1 | 2026-10-19 00:14:35 | 00:16:53 | 2.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.737993 |
| 1 | ri_tvf | 1 | 2026-10-19 00:16:53 | 00:18:41 | 1.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.882586 |
| 1 | ribspc | 1 | 2026-10-19 00:18:41 | 00:19:26 | 0.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0.961476 |
| 1 | asomut | 1 | 2026-10-19 00:19:26 | 00:20:54 | 1.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.097621 |
| 1 | micemp | 1 | 2026-10-19 00:20:54 | 00:22:16 | 1.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.23278 |
| 1 | ri_psp | 1 | 2026-10-19 00:22:16 | 00:26:25 | 4.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1.592264 |
| 1 | ri_transpa | 1 | 2026-10-19 00:26:25 | 00:33:09 | 6.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.073539 |
| 1 | ri_iesinap | 1 | 2026-10-19 00:33:09 | 00:36:04 | 2.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.305139 |
| 1 | ri_msrl | 1 | 2026-10-19 00:36:04 | 00:42:18 | 6.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 2.809107 |
| 1 | ri_iepsp | 1 | 2026-10-19 00:42:18 | 00:48:52 | 6.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.237836 |
| 1 | ri_ai | 1 | 2026-10-19 00:48:52 | 00:52:24 | 3.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.554533 |
| 1 | ri_pspapt | 1 | 2026-10-19 00:52:24 | 00:54:56 | 2.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3.838885 |
| 1 | ri_tsa | 1 | 2026-10-19 00:54:56 | 01:05:58 | 11.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 4.599198 |
| 1 | ri_tar | 1 | 2026-10-19 01:05:58 | 01:08:38 | 2.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 4.868301 |
| 1 | ri_laft | 1 | 2026-10-19 01:08:38 | 01:16:35 | 8.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 5.579745 |
| 1 | ri_dsf | 1 | 2026-10-19 01:16:35 | 01:27:04 | 10.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 6.385675 |
| 1 | ri_nge | 1 | 2026-10-19 01:27:04 | 01:29:13 | 2.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 6.670367 |
| 1 | ri_ot | 1 | 2026-10-19 01:29:13 | 01:33:05 | 3.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 7.079451 |
| 1 | consyr | 1 | 2026-10-19 01:33:05 | 01:38:50 | 5.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 7.640025 |
| 1 | ri_secoexpo | 1 | 2026-10-19 01:38:50 | 01:49:23 | 10.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 8.547851 |
| 1 | seggar | 1 | 2026-10-19 01:49:23 | 02:01:12 | 11.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 9.4721 |
| 1 | ri_sef | 1 | 2026-10-19 02:01:12 | 02:08:06 | 6.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 10.208213 |
| 1 | cedin | 1 | 2026-10-19 02:08:06 | 02:21:30 | 13.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 11.457829 |
| 1 | ri_ii_31_12_19 | 1 | 2026-10-19 02:21:30 | 02:35:20 | 13.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 12.856189 |
| 2 | reqcac | 2 | 2026-10-19 08:43:31 | 08:48:01 | 4.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 13.169338 |
| 2 | cateloc | 2 | 2026-10-19 08:48:01 | 08:58:23 | 10.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 14.181035 |
| 2 | convca | 2 | 2026-10-19 08:58:23 | 09:00:41 | 2.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 14.406939 |
| 2 | socgar | 2 | 2026-10-19 09:00:41 | 09:03:21 | 2.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 14.646175 |
| 2 | horari | 2 | 2026-10-19 09:03:21 | 09:06:33 | 3.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 14.916421 |
| 2 | osapsa | 2 | 2026-10-19 09:06:33 | 09:09:43 | 3.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 15.192453 |
| 2 | snp_atm | 2 | 2026-10-19 09:09:43 | 09:12:01 | 2.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 15.434777 |
| 2 | pognme | 2 | 2026-10-19 09:12:01 | 09:15:31 | 3.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 15.763634 |
| 2 | evacre | 2 | 2026-10-19 09:15:31 | 09:18:53 | 3.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 16.108146 |
| 2 | regpri | 2 | 2026-10-19 09:18:53 | 09:23:08 | 4.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 16.498451 |
| 2 | cescar | 2 | 2026-10-19 09:23:08 | 09:28:51 | 5.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 16.98736 |
| 2 | ctacor | 2 | 2026-10-19 09:28:51 | 09:33:32 | 4.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 17.429584 |
| 2 | fgarcp | 2 | 2026-10-19 09:33:32 | 09:38:20 | 4.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 17.889577 |
| 2 | pscpp | 2 | 2026-10-19 09:38:20 | 09:42:08 | 3.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 18.289265 |
| 2 | secfin | 2 | 2026-10-19 09:42:08 | 09:46:35 | 4.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 18.668495 |
| 2 | incuca | 2 | 2026-10-19 09:46:35 | 09:50:34 | 4.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 19.050411 |
| 2 | venliq | 2 | 2026-10-19 09:50:34 | 09:55:46 | 5.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 19.524507 |
| 2 | fclef | 2 | 2026-10-19 09:55:46 | 09:59:54 | 4.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 19.944665 |
| 2 | lavdin | 2 | 2026-10-19 09:59:54 | 10:05:00 | 5.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 20.46576 |
| 2 | rmrtsd | 2 | 2026-10-19 10:05:00 | 10:14:22 | 9.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 21.264361 |
| 2 | ccbcra | 2 | 2026-10-19 10:14:22 | 10:19:33 | 5.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 21.77495 |
| 2 | apnf | 2 | 2026-10-19 10:19:33 | 10:26:19 | 6.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 22.397194 |
| 2 | traval | 2 | 2026-10-19 10:26:19 | 10:36:57 | 10.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 23.184336 |
| 2 | disres | 2 | 2026-10-19 10:36:57 | 10:48:51 | 11.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 24.144854 |
| 2 | relact | 2 | 2026-10-19 10:48:51 | 10:55:15 | 6.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 24.743891 |
| 2 | coltit | 2 | 2026-10-19 10:55:15 | 11:00:40 | 5.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 25.299006 |
| 2 | raapal | 2 | 2026-10-19 11:00:40 | 11:15:07 | 14.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 26.439945 |
| 2 | servco | 2 | 2026-10-19 11:15:07 | 11:24:07 | 9.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 27.205854 |
| 2 | retype | 2 | 2026-10-19 11:24:07 | 11:29:39 | 5.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 27.757814 |
| 2 | fabcra | 2 | 2026-10-19 11:29:39 | 11:39:18 | 9.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 28.585704 |
| 2 | ri2_ci | 2 | 2026-10-19 11:39:18 | 11:54:57 | 15.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 29.812059 |
| 2 | icmecma | 2 | 2026-10-19 11:54:57 | 12:09:05 | 14.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 30.820393 |
| 2 | pfmipyme | 2 | 2026-10-19 12:09:05 | 12:19:37 | 10.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 31.560766 |
| 2 | prevmi | 2 | 2026-10-19 12:19:37 | 12:34:13 | 14.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 32.831185 |
| 2 | fimipyme | 2 | 2026-10-19 12:34:13 | 12:46:36 | 12.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 33.949868 |
| 2 | garopt | 2 | 2026-10-19 12:46:36 | 12:55:07 | 8.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 34.769194 |
| 2 | actgar | 2 | 2026-10-19 12:55:07 | 13:05:25 | 10.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 35.815279 |
| 2 | gescre | 2 | 2026-10-19 13:05:25 | 13:20:26 | 15.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 37.093272 |
| 2 | snp_mep | 2 | 2026-10-19 13:20:26 | 13:36:47 | 16.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 38.54996 |
| 2 | opecam | 2 | 2026-10-19 13:36:47 | 13:50:27 | 13.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 39.827051 |
| 2 | ordcom | 2 | 2026-10-19 13:50:27 | 14:10:58 | 20.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 40.821077 |
| 2 | gracre | 2 | 2026-10-19 14:10:58 | 14:24:00 | 13.0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 42.091804 |
| 2 | supcon | 2 | 2026-10-19 14:24:00 | 14:35:45 | 11.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 43.301013 |
| 2 | cryl | 2 | 2026-10-19 14:35:45 | 14:49:57 | 14.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 44.600754 |
| 2 | tasint | 2 | 2026-10-19 14:49:57 | 15:02:52 | 12.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 45.869305 |
| 2 | snp_debin | 2 | 2026-10-19 15:02:52 | 15:15:29 | 12.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 47.058929 |
| 2 | afiltr | 2 | 2026-10-19 15:15:29 | 15:38:47 | 23.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 48.96678 |
| 2 | autenf | 2 | 2026-10-19 15:38:47 | 15:53:57 | 15.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 50.427234 |
| 2 | rrci | 2 | 2026-10-19 15:53:57 | 16:09:02 | 15.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 51.85521 |
| 2 | rmgcti | 2 | 2026-10-19 16:09:02 | 16:42:28 | 33.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 54.458129 |
| 2 | repefe | 2 | 2026-10-19 16:42:28 | 16:56:50 | 14.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 55.877259 |
| 2 | snp_psp | 2 | 2026-10-19 16:56:50 | 17:15:30 | 18.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 57.579203 |
| 2 | jafip | 2 | 2026-10-19 17:15:30 | 17:34:56 | 19.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 59.29306 |
| 2 | inspag | 2 | 2026-10-19 17:34:56 | 17:52:09 | 17.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 60.974401 |
| 2 | graloc | 2 | 2026-10-19 17:52:09 | 18:12:21 | 20.2 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 63.00929 |
| 2 | adfsp | 2 | 2026-10-19 18:12:21 | 18:32:02 | 19.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 64.890696 |
| 2 | seguef | 2 | 2026-10-19 18:32:02 | 18:50:38 | 18.6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 66.787392 |
| 2 | garant | 2 | 2026-10-19 18:50:38 | 19:09:27 | 18.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 68.719952 |
| 2 | snp_cec | 2 | 2026-10-19 19:09:27 | 19:33:10 | 23.7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 71.023663 |
| 2 | snp_spd | 2 | 2026-10-19 19:33:10 | 19:55:19 | 22.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 73.306782 |
| 2 | snp_dd | 2 | 2026-10-19 19:55:19 | 20:21:24 | 26.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 75.705769 |
| 2 | ratio | 2 | 2026-10-19 20:21:24 | 20:52:41 | 31.3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 78.514054 |
| 2 | ratiofn | 2 | 2026-10-19 20:52:41 | 21:19:27 | 26.8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 81.144215 |
| 2 | finsec | 2 | 2026-10-19 21:19:27 | 21:51:51 | 32.4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 84.187337 |
| 2 | snp_tr_nc | 2 | 2026-10-19 21:51:51 | 22:19:00 | 27.1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 86.521545 |
| 2 | pimf | 2 | 2026-10-19 22:19:00 | 22:50:29 | 31.5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 89.500136 |
| 2 | depinv | 2 | 2026-10-19 22:50:29 | 23:22:23 | 31.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 92.726101 |
| 2 | ctavis | 2 | 2026-10-19 23:22:23 | 00:11:16 | 48.9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 97.598343 |

La pasada del lanzamiento 2 por el tramo 1: 30 TOs, rc [0], freno ['OK'], gasto global [12.856189] (sin gasto nuevo), de 2026-10-19 08:42:27 a 08:43:30.

## 5. La salida de `resumen_t2.py`, completa

`<repo>/.venv/bin/python -B data/experiment/tanda_final/t2/resumen_t2.py --repo "$PWD" --out data/experiment/tanda_final/t2/resumen_t2_final.json`,
con sus valores por defecto, rc 0 (`t2/resumen_t2_final.txt`). Las líneas del runner que toma son 128, todas de «corrida completa»: 30 del
lanzamiento 1 y 98 del lanzamiento 2; ninguna `FRENO:` ni `ERROR:`.

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
reqcac         3      3      3     0    0      0      0    T     T    0.3131
cateloc       11     11      8     3    0      0      0    T     T    1.0117
convca        12     12     12     0    0      0      0    T     T    0.2259
socgar        12     12     12     0    0      0      0    T     T    0.2392
horari        13     13     13     0    0      0      0    T     T    0.2702
osapsa        13     13     13     0    0      0      0    T     T    0.2760
snp_atm       16     16     16     0    0      0      0    T     T    0.2423
pognme        17     17     17     0    0      0      0    T     T    0.3289
evacre        19     19     18     1    0      0      0    T     T    0.3445
regpri        20     20     16     4    0      0      0    T     T    0.3903
cescar        21     21     19     2    0      0      0    T     T    0.4889
ctacor        21     21     21     0    0      0      0    T     T    0.4422
fgarcp        22     22     22     0    0      0      0    T     T    0.4600
pscpp         22     22     22     0    0      0      0    T     T    0.3997
secfin        22     22     20     2    0      0      0    T     T    0.3792
incuca        23     23     23     0    0      0      0    T     T    0.3819
venliq        23     23     23     0    0      0      0    T     T    0.4741
fclef         28     28     28     0    0      0      0    T     T    0.4202
lavdin        29     29     28     1    0      0      0    T     T    0.5211
rmrtsd        31     31     31     0    0      0      0    T     T    0.7986
ccbcra        32     32     32     0    0      0      0    T     T    0.5106
apnf          34     34     33     1    0      0      0    T     T    0.6222
traval        35     35     34     1    0      0      0    T     T    0.7871
disres        38     38     35     3    0      0      0    T     T    0.9605
relact        38     38     38     0    0      0      0    T     T    0.5990
coltit        39     39     39     0    0      0      0    T     T    0.5551
raapal        40     40     38     2    0      0      0    T     T    1.1409
servco        40     40     39     1    0      0      0    T     T    0.7659
retype        41     41     40     1    0      0      0    T     T    0.5520
fabcra        42     42     40     2    0      0      0    T     T    0.8279
ri2_ci        45     45     45     0    0      0      0    T     T    1.2264
icmecma       48     48     48     0    0      0      0    T     T    1.0083
pfmipyme      52     52     52     0    0      0      0    T     T    0.7404
prevmi        52     52     51     1    0      0      0    T     T    1.2704
fimipyme      55     55     53     2    0      0      0    T     T    1.1187
garopt        55     55     54     1    0      0      0    T     T    0.8193
actgar        60     60     60     0    0      0      0    T     T    1.0461
gescre        61     61     60     1    0      0      0    T     T    1.2780
snp_mep       62     62     62     0    0      0      0    T     T    1.4567
opecam        65     65     65     0    0      0      0    T     T    1.2771
ordcom        65     65     65     0    0      0      0    T     T    0.9940
gracre        67     67     66     1    0      0      0    T     T    1.2707
supcon        67     67     67     0    0      0      0    T     T    1.2092
cryl          68     68     67     1    0      0      0    T     T    1.2997
tasint        69     69     68     1    0      0      0    T     T    1.2686
snp_debin     71     71     71     0    0      0      0    T     T    1.1896
afiltr        72     72     71     1    0      0      0    T     T    1.9079
autenf        75     75     72     3    0      0      0    T     T    1.4605
rrci          77     77     77     0    0      0      0    T     T    1.4280
rmgcti        81     81     80     1    0      0      0    T     T    2.6029
repefe        87     87     86     1    0      0      0    T     T    1.4191
snp_psp       89     89     89     0    0      0      0    T     T    1.7019
jafip         91     91     89     2    0      0      0    T     T    1.7139
inspag        93     93     93     0    0      0      0    T     T    1.6813
graloc       100    100     99     1    0      0      0    T     T    2.0349
adfsp        101    101    100     1    0      0      0    T     T    1.8814
seguef       101    101    101     0    0      0      0    T     T    1.8967
garant       106    106    106     0    0      0      0    T     T    1.9326
snp_cec      122    122    119     3    0      0      0    T     T    2.3037
snp_spd      130    130    129     1    0      0      0    T     T    2.2831
snp_dd       131    131    131     0    0      0      0    T     T    2.3990
ratio        133    133    128     5    0      0      0    T     T    2.8083
ratiofn      133    133    130     3    0      0      0    T     T    2.6302
finsec       134    134    128     6    0      0      0    T     T    3.0431
snp_tr_nc    136    136    136     0    0      0      0    T     T    2.3342
pimf         165    165    164     1    0      0      0    T     T    2.9786
depinv       203    203    201     2    0      0      0    T     T    3.2260
ctavis       271    271    267     4    0      0      0    T     T    4.8722
total       4951   4951   4870    80    1      0      0
gasto global USD 97.5983 de un tope de USD 151.5835 (dentro del tope); TOs con las dos fases cerradas: 98
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
[ri_bdp] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_ieccm] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_rcl] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_esd] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[verac] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_acsf] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_cr] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_tvf] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ribspc] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[asomut] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[micemp] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_psp] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_transpa] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_iesinap] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_msrl] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_iepsp] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_ai] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_pspapt] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_tsa] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_tar] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_laft] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_dsf] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_nge] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_ot] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[consyr] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_secoexpo] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[seggar] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_sef] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[cedin] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[ri_ii_31_12_19] corrida completa: gasto global=USD 12.8562 | wall=0.0 min
[reqcac] corrida completa: gasto global=USD 13.1693 | wall=4.5 min
[cateloc] corrida completa: gasto global=USD 14.1810 | wall=10.3 min
[convca] corrida completa: gasto global=USD 14.4069 | wall=2.3 min
[socgar] corrida completa: gasto global=USD 14.6462 | wall=2.6 min
[horari] corrida completa: gasto global=USD 14.9164 | wall=3.2 min
[osapsa] corrida completa: gasto global=USD 15.1925 | wall=3.1 min
[snp_atm] corrida completa: gasto global=USD 15.4348 | wall=2.3 min
[pognme] corrida completa: gasto global=USD 15.7636 | wall=3.5 min
[evacre] corrida completa: gasto global=USD 16.1081 | wall=3.3 min
[regpri] corrida completa: gasto global=USD 16.4985 | wall=4.2 min
[cescar] corrida completa: gasto global=USD 16.9874 | wall=5.7 min
[ctacor] corrida completa: gasto global=USD 17.4296 | wall=4.6 min
[fgarcp] corrida completa: gasto global=USD 17.8896 | wall=4.8 min
[pscpp] corrida completa: gasto global=USD 18.2893 | wall=3.8 min
[secfin] corrida completa: gasto global=USD 18.6685 | wall=4.4 min
[incuca] corrida completa: gasto global=USD 19.0504 | wall=3.9 min
[venliq] corrida completa: gasto global=USD 19.5245 | wall=5.2 min
[fclef] corrida completa: gasto global=USD 19.9447 | wall=4.1 min
[lavdin] corrida completa: gasto global=USD 20.4658 | wall=5.1 min
[rmrtsd] corrida completa: gasto global=USD 21.2644 | wall=9.3 min
[ccbcra] corrida completa: gasto global=USD 21.7749 | wall=5.1 min
[apnf] corrida completa: gasto global=USD 22.3972 | wall=6.7 min
[traval] corrida completa: gasto global=USD 23.1843 | wall=10.5 min
[disres] corrida completa: gasto global=USD 24.1449 | wall=11.8 min
[relact] corrida completa: gasto global=USD 24.7439 | wall=6.4 min
[coltit] corrida completa: gasto global=USD 25.2990 | wall=5.4 min
[raapal] corrida completa: gasto global=USD 26.4399 | wall=14.4 min
[servco] corrida completa: gasto global=USD 27.2059 | wall=9.0 min
[retype] corrida completa: gasto global=USD 27.7578 | wall=5.5 min
[fabcra] corrida completa: gasto global=USD 28.5857 | wall=9.6 min
[ri2_ci] corrida completa: gasto global=USD 29.8121 | wall=15.6 min
[icmecma] corrida completa: gasto global=USD 30.8204 | wall=14.0 min
[pfmipyme] corrida completa: gasto global=USD 31.5608 | wall=10.4 min
[prevmi] corrida completa: gasto global=USD 32.8312 | wall=14.5 min
[fimipyme] corrida completa: gasto global=USD 33.9499 | wall=12.3 min
[garopt] corrida completa: gasto global=USD 34.7692 | wall=8.5 min
[actgar] corrida completa: gasto global=USD 35.8153 | wall=10.3 min
[gescre] corrida completa: gasto global=USD 37.0933 | wall=15.0 min
[snp_mep] corrida completa: gasto global=USD 38.5500 | wall=16.3 min
[opecam] corrida completa: gasto global=USD 39.8271 | wall=13.6 min
[ordcom] corrida completa: gasto global=USD 40.8211 | wall=20.4 min
[gracre] corrida completa: gasto global=USD 42.0918 | wall=13.0 min
[supcon] corrida completa: gasto global=USD 43.3010 | wall=11.7 min
[cryl] corrida completa: gasto global=USD 44.6008 | wall=14.1 min
[tasint] corrida completa: gasto global=USD 45.8693 | wall=12.9 min
[snp_debin] corrida completa: gasto global=USD 47.0589 | wall=12.6 min
[afiltr] corrida completa: gasto global=USD 48.9668 | wall=23.2 min
[autenf] corrida completa: gasto global=USD 50.4272 | wall=15.1 min
[rrci] corrida completa: gasto global=USD 51.8552 | wall=15.0 min
[rmgcti] corrida completa: gasto global=USD 54.4581 | wall=33.4 min
[repefe] corrida completa: gasto global=USD 55.8773 | wall=14.3 min
[snp_psp] corrida completa: gasto global=USD 57.5792 | wall=18.6 min
[jafip] corrida completa: gasto global=USD 59.2931 | wall=19.4 min
[inspag] corrida completa: gasto global=USD 60.9744 | wall=17.2 min
[graloc] corrida completa: gasto global=USD 63.0093 | wall=20.2 min
[adfsp] corrida completa: gasto global=USD 64.8907 | wall=19.6 min
[seguef] corrida completa: gasto global=USD 66.7874 | wall=18.5 min
[garant] corrida completa: gasto global=USD 68.7200 | wall=18.8 min
[snp_cec] corrida completa: gasto global=USD 71.0237 | wall=23.7 min
[snp_spd] corrida completa: gasto global=USD 73.3068 | wall=22.1 min
[snp_dd] corrida completa: gasto global=USD 75.7058 | wall=26.0 min
[ratio] corrida completa: gasto global=USD 78.5141 | wall=31.2 min
[ratiofn] corrida completa: gasto global=USD 81.1442 | wall=26.7 min
[finsec] corrida completa: gasto global=USD 84.1873 | wall=32.3 min
[snp_tr_nc] corrida completa: gasto global=USD 86.5215 | wall=27.1 min
[pimf] corrida completa: gasto global=USD 89.5001 | wall=31.4 min
[depinv] corrida completa: gasto global=USD 92.7261 | wall=31.8 min
[ctavis] corrida completa: gasto global=USD 97.5983 | wall=48.8 min
```

- **Por tramo** (tabla 4): el tramo 1, 601 unidades, 587 aceptadas, 13 en la cola y 1 error; el tramo 2, 4.350 unidades, 4.283
  aceptadas, 67 en la cola y 0 errores. En los dos, 0 sin destino y 0 ids repetidos, cobertura completa y exacta de la E0, y las dos fases
  cerradas en los 98. Las unidades con partes son las mismas 4.951: ninguna unidad se partió por corte.

## 6. `conteos_t2.py` y los `NO_ABRIR_`

`<repo>/.venv/bin/python -B data/experiment/tanda_final/t2/conteos_t2.py --repo "$PWD"`, con sus valores por defecto, rc 0
(`t2/conteos_t2_final.txt`; pisa el `NO_ABRIR_` de conteos del FRENO parcial 1, que era `e3616d66…`):

```
sha256 eccd8fa3d8b878299f4793d642c6f6b8a6a0a4cb5a924de73358d31896075047
vigilancia integridad_e3: OK
```

Los dos `NO_ABRIR_`, que no abrí (solo su sha256):

```
089d9ff54611ca9c30e902e7f2175a020a2685884c68682828b37e2a23f8a755  data/experiment/tanda_final/t2/NO_ABRIR_salida_e3_tanda_final.txt
eccd8fa3d8b878299f4793d642c6f6b8a6a0a4cb5a924de73358d31896075047  data/experiment/tanda_final/t2/NO_ABRIR_conteos_reextracciones_tanda_final.json
```

## 7. El costo y la duración (tablas 5, 6 y 7)

|  | gasto real | §3 del pre-registro | U × tarifa | líneas de A3 | §3 + líneas | real / (§3 + líneas) | repartido | real / repartido |
|---|---|---|---|---|---|---|---|---|
| tramo 1 | 12.856189 | 12.6901 | 12.690115 | 0.088479 | 12.778594 | 1.0061 | 19.310012 | 0.6658 |
| tramo 2 | 84.742154 | 91.8502 | 91.850250 | 0.120959 | 91.971209 | 0.9214 | 85.439791 | 0.9918 |
| total | 97.598343 | 104.5404 | 104.540365 | 0.209438 | 104.749803 | 0.9317 | 104.749803 | 0.9317 |

Contra el tope de USD 151.5835: 0.6439 del tope, con un margen de 53.985157. El gasto por TO sumado da 97.598343 y el global del runner, 97.598343.

Por TO, real / (§3 + líneas): de ('ri_nge', Decimal('0.4456')) a ('reqcac', Decimal('4.9008')); real / repartido: de ('ri_psp', Decimal('0.2162')) a ('ri_nge', Decimal('4.0737')).

- **El gasto real, USD 97,598343, es 0,9317 del estimado** (U × 0,021115 más las líneas de alcance, 104,749803, el USD 104,7498 del
  §3), igual con las cifras del §3 y con el reparto del manifiesto, que tienen el mismo total.
- **Por tramo, con las cifras del §3 más las líneas:** el tramo 1, 1,0061 (12,856189 contra 12,778594); el tramo 2, 0,9214 (84,742154
  contra 91,971209). **Con el reparto:** el tramo 1, 0,6658 (contra 19,310012); el tramo 2, 0,9918 (contra 85,439791).
- **Contra el tope:** 0,6439 de USD 151,5835, con un margen de 53,985157. Lejos de los USD 341 del total.
- **Por TO** (tabla 5): lo real va de 0,4456 (ri_nge) a 4,9008 (reqcac) veces el §3 más las líneas, y de 0,2162 (ri_psp) a 4,0737
  (ri_nge) veces el repartido.

|  | real (min) | proyectado por unidades (min) | proyectado por caracteres (min) |
|---|---|---|---|
| tramo 1 (suma de sus TOs, lanzamiento 1) | 146.7 | 148.6 | 183.5 |
| tramo 2 (suma de sus TOs, lanzamiento 2) | 927.9 | 1075.3 | 812.0 |
| los dos lanzamientos, de inicio a fin | [146.6, 928.9] → 1075.5 | 1223.8 | 995.5 |

Entre el fin del lanzamiento 1 (2026-10-19T02:35:20-0300) y el inicio del 2 (2026-10-19T08:42:24-0300): 6 h 7 min 4 s, que no cuentan. La pasada del lanzamiento 2 por el tramo 1: 1.05 min.

- La duración real son los dos lanzamientos, de inicio a fin: 146,6 y 928,9 min, 1.075,5 en total, contra 1.223,8 proyectados por
  unidades y 995,5 por caracteres. Entre los dos lanzamientos pasaron 6 h 7 min 4 s (de las 02:35:20 a las 08:42:24) por el FRENO y la
  decisión; no cuentan. La pasada del lanzamiento 2 por el tramo 1 tardó 1,05 min, sin gasto (tabla 7, al pie).

## 8. La foto del repo, los commits, los `.pyc` y el grep (tablas 8 y 8b)

| cifra | valor |
|---|---|
| antes (inicio, fin, entradas, sin abrir, enlaces) | ['2026-10-19 00:08:03', '2026-10-19 00:08:15', 53296, 40, 342] |
| después (inicio, fin, entradas, sin abrir, enlaces) | ['2026-10-20 00:12:30', '2026-10-20 00:12:43', 55304, 42, 342] |
| nuevos, por carpeta | {'de los commits de la autora u otra unidad': 45, 'data/experiment/reextraccion_v2/corpus_tanda_final/': 1943, 'data/experiment/tanda_final/t2/': 20} |
| borrados | {} |
| cambiados, por carpeta | {'de los commits de la autora u otra unidad': 5, 'data/experiment/reextraccion_v2/e1_extractor/cache/': 1, 'data/experiment/reextraccion_v2/e3_verificador/cache/': 2, 'logs/cache_usage.jsonl': 1} |
| commits de la autora en el período | 12 |
| rutas ajenas a T2, por commit (nuevas) | {'commit 06a2deef': 2, 'commit 7cb770bd': 40, 'commit 593e5db2': 1, 'commit 123111e6': 1, 'commit a92bddb0, a7d00025': 1} |
| rutas ajenas a T2, por commit (cambiadas) | {'commit 7d506d29': 1, 'commit 24007f15': 1, 'commit 7cb770bd, 593e5db2': 1, 'commit 86541475': 1, 'commit 729dc565, 9950be88, 86541475, a92bddb0, 7cb770bd, 123111e6, a7d00025, 593e5db2, 06a2deef, 7d506d29, 68db7c92': 1} |
| rutas ajenas a T2 sin commit | {'nuevos': [], 'borrados': [], 'cambiados': []} |

| hash | asunto |
|---|---|
| 729dc565 | Registro de decisiones: los minutos del piloto y del pool, el sello del pool y lo pago siempre en secuencia, nunca al lado de una extraccion |
| 9950be88 | Registro de decisiones: la paginacion de las busquedas del banco, el pie que dice desde donde seguir y la regresion antes de la medicion de familias |
| 86541475 | Pre-registro de la tanda final: la nota del modulo de referencias, que entra despues del sello, y las decisiones del juez, la cobertura y el banco en paralelo |
| a92bddb0 | Preguntas de la evaluacion final: las notas de la primera etapa y de las corridas por pregunta, y el presupuesto como techo de trabajo |
| 7cb770bd | Tripletas: el sorteo de la etapa de validacion, sellado antes de leer, con sus notas al pie y las decisiones de la tarde |
| 123111e6 | Juez de la evaluacion final: el mandato firmado, con el juez como esta y su verificacion sobre la corrida por fragmentos |
| a7d00025 | Preguntas de la evaluacion final: el mandato firmado sin abstencion, con la caida por clase y cuatro preguntas por documento |
| 593e5db2 | Tripletas y registro de decisiones: la segunda enmienda firmada, y la union de comunicaciones con la re-aplicacion unica antes del sello |
| 06a2deef | Registro de decisiones y calibradores de la desambiguacion: la hoja marcada y su sello, y el diseno de las preguntas nuevas por tipo |
| 24007f15 | Reprocesamiento r2b: el ancla del candado del mensaje del extractor, al dia en tres filas |
| 7d506d29 | Registro de decisiones y backlog: las unidades que el reintento por forma deja sin extraer se declaran, y su arreglo va al backlog |
| 68db7c92 | Registro de decisiones: el control entre tramos de la ultima tanda en freno, y el segundo tramo autorizado por la autora |

- **La foto después** (20/10/2026, 00:12:30 a 00:12:43, el mismo script): 55.304 entradas, 42 sin abrir y 342 enlaces; **2.008 nuevos,
  0 borrados y 9 cambiados.**
  - **Lo de T2:** 1.943 nuevos en `data/experiment/reextraccion_v2/corpus_tanda_final/` y 20 en `data/experiment/tanda_final/t2/` (los
    dos `NO_ABRIR_`, `avance_t2.jsonl`, el JSON del control, el FRENO parcial 1, los scripts y salidas de sus cifras y de la
    identificación, las salidas de `resumen_t2.py` y `conteos_t2.py` del tramo 1 y del final, y el log del lanzamiento 1); cambiados,
    las tres bases de la caché y `logs/cache_usage.jsonl`. Este FRENO, el script de sus cifras con sus salidas y el log del lanzamiento 2
    son posteriores a la foto.
  - **Las tres bases y `logs/cache_usage.jsonl`, solo por su tamaño y su fecha** (`stat`, a las 00:12): `e1_extraccion.db`, 1.151.258.624
    bytes, 23:56:13; `e1_reintentos.db`, 105.365.504 bytes, 00:11:12; `e3_verificacion.db`, 577.253.376 bytes, 00:11:12;
    `cache_usage.jsonl`, 7.766.905 bytes, 00:11:12.
  - **Lo que entró por los commits de la autora** (no es mío), por script, ruta por ruta con `git log 27bfaeb5..HEAD -- <ruta>`: 45 rutas
    nuevas (40 de `7cb770bd`, 2 de `06a2deef` y 1 de `593e5db2`, de `123111e6` y de `a92bddb0` con `a7d00025`) y 5 cambiadas (el backlog,
    la tabla de reprocesamiento, el pre-registro de las tripletas, el de la tanda final y el registro de decisiones). **Ninguna ruta
    cambió sin un commit que la explique.**
  - **`data/experiment/neo4j/volumen/`:** sin cambios.
  - Los 40 sin abrir de antes, con el mismo tamaño y la misma fecha; los 2 nuevos son los `NO_ABRIR_` de `t2/`.
- **Los `.pyc`:** 11.236 líneas antes y 11.236 después, iguales (`diff` vacío).
- **Lo que leyó la foto:** el script de la foto, el de T1 como pide el «seguí», calcula el sha256 de cada archivo del repo: leyó los de la
  salida del runner, los cuatro de la caché y los que entraron por los commits de la autora (entre ellos, documentos de B6.3 y archivos
  de las tripletas), sin mostrar su contenido. De la comparación miré solo rutas y cuentas por carpeta; los nombres de las rutas de los
  commits salieron en la consola de la sesión al clasificarlas. Las fotos enteras y su comparación no van al paquete.
- **El grep de convenciones:** sobre los 29 archivos de `data/experiment/tanda_final/t2/` que no son `NO_ABRIR_` (antes de
  completar este punto). Los tokens del nombre salen de `git config user.name` en la consola y no quedan escritos en ningún archivo,
  más la lista de términos de la sección 11 del FRENO T1, con `grep -c -i -E`. **Ninguno con una cuenta distinta de 0.** Rutas con
  `/Users/` o `/private/tmp`: solo el renglón del FRENO parcial 1 que cita ese mismo patrón. El control positivo da 1.

## 9. La prueba del acumulado con el tramo 1 (registro, §42)

Por indicación de la autora, la hace la mesa aparte, sobre una copia, cuando el control entre tramos dé OK. No la corrí. Los dos
controles dieron FRENO.

## 10. Para la autora

1. **`ri_transpa::Sbloque1::chapeau_seccion`** queda sin extraer, declarada, para su mandato aparte (sección 2).
2. **La cola:** 80 unidades (13 del tramo 1 y 67 del tramo 2), para su lectura según el §6 del pre-registro.
3. **El costo** quedó en 0,9317 del estimado y 0,6439 del tope; el reparto sobreestimó el tramo 1 (0,6658) y acertó el tramo 2 (0,9918).
4. **La pausa del viernes 23/10 a las 18:00** no hizo falta: la tanda terminó el 20/10 a las 00:11.

## 11. Errores propios, con su causa

1. **Un archivo en `/tmp`** (FRENO T2 parcial 1, sección 9): en el paso 0, un comando mandó la salida de `shasum -a 256 -c` a
   `/tmp/null_t2_check` y lo borró en el mismo comando, fuera del scratchpad. No afectó ninguna cifra.
2. **Una columna de la tabla 6** salía de restar el §3 redondeado a cuatro decimales (las líneas del tramo 1 daban 0,088494 en lugar de
   0,088479). Lo corregí antes de este FRENO: las líneas se restan de U × tarifa exacto, y el §3 del pre-registro va en su propia columna.

## 12. El paquete

`revision_tanda_final_FRENO_T2/`, en el scratchpad de la sesión (`afadde2e-6298-47fb-9777-7fcb43152d50`), con su `manifest.txt` (sha256
y una línea por archivo). Lleva este FRENO, el parcial 1, la identificación, los scripts de las cifras con sus salidas, las de
`resumen_t2.py` y `conteos_t2.py`, el registro de avance, el JSON del control, los dos logs, la consulta de deprecaciones, el lanzador,
el resumen de las fotos, los `.pyc` y el checkpoint. No lleva los `NO_ABRIR_`, nada de la salida del runner ni las fotos enteras. Su
copia con `ditto` está en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T2/`;
la verificación va en el mensaje del FRENO.

FRENO T2. Espero la revisión de la autora.
