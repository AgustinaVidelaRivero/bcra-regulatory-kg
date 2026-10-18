# FRENO T2 — tanda 1 de B6.1: la extracción E1 a E3 de los 20 TOs, completa (17/10/2026, sin commit)

Rigen el §2, el §3, el §4.2 y el §7 del pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota al pie del
17/10/2026 en `ca5b39fd`). HEAD `ca5b39fd`.

**Resultado: el tercer lanzamiento terminó con 0, y los 20 TOs están completos.**
- 3.290 unidades, 3.294 con las partes por corte.
- 3.252 aceptadas, 42 en cola y 0 errores; cobertura completa y 0 ids repetidos.
- **Gasto:** USD 70,991032, contra el estimado de 69,659193 (1,0191 veces) y el tope de 100,7291 (el 70,48 %).
- El freno por modelo dio OK después de cada TO, con E1 `claude-haiku-4-5-20251001` y E3 `claude-sonnet-5`.
- Nada commiteado y ningún mensaje de commit preparado: el commit es de la autora y queda PENDIENTE.

## 0. Los tres lanzamientos y las decisiones entre ellos

| lanz. | inicio | fin | min | pid | salida | qué pasó |
|---:|---|---|---:|---:|---:|---|
| 1 | 16/10 20:48:13 | 16/10 21:01:43 | 13,5 | 76009 | 3 | freno por proyección en ri_pgn:e3 (`FRENO_T2_parcial_1.md`, `49e2dca8…`) |
| 2 | 16/10 23:34:21 | 17/10 00:17:08 | 42,8 | 25724 | 3 | freno por proyección en ri_rml:e1 (`FRENO_T2_parcial_2.md`, `144be679…`) |
| 3 | 17/10 08:15:22 | 17/10 20:52:20 | 757,0 | 29101 | **0** | los 20 completos |

- **Después del lanzamiento 1, la autora** decidió relanzar con el mismo tope y el mismo comando (§4.2).
- **Después del lanzamiento 2, la autora** decidió repartir el estimado por TO por caracteres de E0, con el mismo total, el mismo tope y la
  misma tarifa (§4.2; `ca5b39fd`).
- **Lo que cambió `ca5b39fd`:** solo `limites.estimado_usd` del manifiesto, que pasó de `4dd02505…` a `818a62cf…`; también
  `sha256_para_T2.txt` y el sha256 esperado en `lanzar_t2.py`. Lo controlé en solo lectura: el total sigue en 69,659193, y el tope, el
  orden, los TOs y los sellos no cambian.
- **Los dos parciales** están renombrados sin cambios: `FRENO_T2_parcial_1.md` (`49e2dca8…`) y `FRENO_T2_parcial_2.md` (`144be679…`). El
  paso 0 del «seguí» está en el parcial 1.

## 1. Los controles antes del lanzamiento 3 (17/10/2026, 08:14:24)

```
$ git log -1 --format='%s'
Primera tanda: el estimado de la extraccion repartido entre sus documentos por caracteres, con el mismo total y el mismo tope
$ git status --porcelain --untracked-files=no
$ shasum -a 256 data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json
818a62cfde403a453d0551916022f928f7cd9cb62d7947801eadb587f2385d9d  data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json
$ shasum -a 256 -c data/experiment/tanda1/t1/sha256_para_T2.txt | awk '{print $NF}' | sort | uniq -c
 108 OK
$ pgrep -fl "runner_corpus.py|lanzar_t2.py"
(rc=1)
$ tail -1 data/experiment/tanda1/t2/avance_t2.jsonl
{"evento": "fin_lanzador", "ts": "2026-10-17T00:17:08-0300", "copia_de_las_bases_borrada": true}
no existe: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_3
```

- El último commit es `ca5b39fd`.
- `git status` y `pgrep` salieron vacíos, y `shasum -c` dio 0 distintos.
- **La foto antes del lanzamiento 3** (`t2/foto_repo_tanda1_t2.py`, de 08:14:57 a 08:15:08): 51.267 entradas. Los `.pyc`: 11.236 líneas.
- `df -k .`: 221.352.724 KB libres.

## 2. El lanzamiento 3

Desde la raíz del repo, en segundo plano (`run_in_background`), una sola vez, sin `--stub`, `--solo-tos` ni `--git-repo`:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases "$HOME/INGENIERIA IA/TESIS/fuera_del_repo/trabajo_t2_tanda1/bases_lanzamiento_3"
```

- **Inicio:** 08:15:22 (`inicio_lanzador`, pid 29101). **Fin:** 20:52:20 (`fin_lanzador`). **Código de salida: 0** (la app avisó «exited
  with code 0»).
- **`controles_previos`** (08:15:23), todo OK:
  - el piso: 221.342.364 KB libres, contra 31.457.280;
  - las rutas: `HEAD:  78 de 78`, `árbol: 78 de 78`;
  - el SDK: `0.100.0`;
  - el sha256 del manifiesto, que es `818a62cf…`, y el tope;
  - la carpeta de trabajo, fuera del repo y nueva.
- **`freno_modelo_antes`** (08:15:24): OK, con `claude-haiku-4-5-20251001` / `claude-sonnet-5`.
- **El primer TO con trabajo nuevo:** ri_rml, a las 08:15:29 (su E3).
- **El cierre:** el último renglón es `{"evento": "fin_lanzador", "ts": "2026-10-17T20:52:20-0300", "copia_de_las_bases_borrada": true}`.
- **La copia de trabajo de las bases:** borrada en los tres lanzamientos (`copia_de_las_bases_borrada: true`). `ls` de `bases_lanzamiento_3`
  da «No such file or directory».

## 3. Por TO, los renglones de los tres lanzamientos (`avance_t2.jsonl`, sha256 `0be260e5…`)

| lanz. | TO | inicio | fin | min | rc | freno por modelo | ids de E1 | ids de E3 | gasto global USD |
|---:|---|---|---|---:|---:|---|---|---|---:|
| 1 | ri_gerc | 20:48:15 | 20:51:33 | 3,3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 0,352899 |
| 1 | ri_pgn | 20:51:33 | 21:01:43 | 10,2 | 3 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ri_gerc | 23:34:23 | 23:34:24 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ri_pgn | 23:34:24 | 23:34:26 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,149063 |
| 2 | ceninf | 23:34:26 | 23:42:17 | 7,8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 1,957244 |
| 2 | ri_rml | 23:42:17 | 00:17:08 | 34,9 | 3 | OK | claude-haiku-4-5-20251001 | (vacío) | 3,664724 |
| 3 | ri_gerc | 08:15:24 | 08:15:25 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3,664724 |
| 3 | ri_pgn | 08:15:25 | 08:15:27 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3,664724 |
| 3 | ceninf | 08:15:27 | 08:15:29 | 0,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 3,664724 |
| 3 | ri_rml | 08:15:29 | 08:25:08 | 9,7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 5,008249 |
| 3 | nmcief | 08:25:08 | 08:47:59 | 22,9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 6,775916 |
| 3 | adrei | 08:47:59 | 08:59:59 | 12,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 8,052002 |
| 3 | opefci | 08:59:59 | 09:11:40 | 11,7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 9,229012 |
| 3 | ri_dcpc | 09:11:40 | 09:38:45 | 27,1 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 11,382106 |
| 3 | snp_tr | 09:38:45 | 10:06:11 | 27,4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 13,824134 |
| 3 | efemin | 10:06:11 | 10:37:41 | 31,5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 16,767601 |
| 3 | ri_mmsef | 10:37:41 | 10:52:57 | 15,3 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 18,677987 |
| 3 | manori | 10:52:57 | 11:45:23 | 52,4 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 22,804662 |
| 3 | expaef | 11:45:23 | 12:09:20 | 23,9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 25,439699 |
| 3 | ri_ccna | 12:09:20 | 12:46:10 | 36,8 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 28,958426 |
| 3 | ayccef | 12:46:10 | 13:21:41 | 35,5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 32,591539 |
| 3 | cirmo3 | 13:21:41 | 14:18:15 | 56,6 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 37,878350 |
| 3 | snp_cheq | 14:18:15 | 15:28:47 | 70,5 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 43,941846 |
| 3 | cajasc | 15:28:47 | 16:28:46 | 60,0 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 49,675703 |
| 3 | depaho | 16:28:46 | 18:12:26 | 103,7 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 57,921399 |
| 3 | lingeef | 18:12:26 | 20:52:20 | 159,9 | 0 | OK | claude-haiku-4-5-20251001 | claude-sonnet-5 | 70,991032 |

- La tabla sale por script de `avance_t2.jsonl`, con el gasto global de cada renglón con sus 6 decimales.
- En los lanzamientos 2 y 3, los TOs con las fases ya cerradas solo corrieron su E2, que es offline, sin gasto.

## 4. La salida de `resumen_t2.py`, completa

`.venv/bin/python -B data/experiment/tanda1/t2/resumen_t2.py --repo . --out data/experiment/tanda1/t2/resumen_t2.json` (rc 0;
`resumen_t2.json`, sha256 `b4453e5f…`):

```
TO          unid c/part  acept  cola  err s/dest idsrep  cob cobE0     gasto
ri_gerc       15     15     15     0    0      0      0    T     T    0.3529
ri_pgn        21     21     20     1    0      0      0    T     T    0.7962
ceninf        39     39     39     0    0      0      0    T     T    0.8082
ri_rml        46     50     47     3    0      0      0    T     T    3.0510
nmcief        55     55     55     0    0      0      0    T     T    1.7677
adrei         70     70     70     0    0      0      0    T     T    1.2761
opefci        74     74     74     0    0      0      0    T     T    1.1770
ri_dcpc       75     75     74     1    0      0      0    T     T    2.1531
snp_tr       103    103    101     2    0      0      0    T     T    2.4420
efemin       119    119    116     3    0      0      0    T     T    2.9435
ri_mmsef     128    128    128     0    0      0      0    T     T    1.9104
manori       152    152    148     4    0      0      0    T     T    4.1267
expaef       165    165    165     0    0      0      0    T     T    2.6350
ri_ccna      169    169    163     6    0      0      0    T     T    3.5187
ayccef       196    196    196     0    0      0      0    T     T    3.6331
cirmo3       256    256    254     2    0      0      0    T     T    5.2868
snp_cheq     265    265    264     1    0      0      0    T     T    6.0635
cajasc       287    287    284     3    0      0      0    T     T    5.7339
depaho       442    442    436     6    0      0      0    T     T    8.2457
lingeef      613    613    603    10    0      0      0    T     T   13.0696
total       3290   3294   3252    42    0      0      0
gasto global USD 70.9910 de un tope de USD 100.7291 (dentro del tope); TOs con las dos fases cerradas: 20
[ri_gerc] corrida completa: gasto global=USD 0.3529 | wall=3.3 min
[ri_pgn] FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21
[ri_gerc] corrida completa: gasto global=USD 1.1491 | wall=0.0 min
[ri_pgn] corrida completa: gasto global=USD 1.1491 | wall=0.0 min
[ceninf] corrida completa: gasto global=USD 1.9572 | wall=7.8 min
[ri_rml] FRENO: proyección USD 122.79 supera el tope global USD 100.73 en ri_rml:e1 50/50
[ri_gerc] corrida completa: gasto global=USD 3.6647 | wall=0.0 min
[ri_pgn] corrida completa: gasto global=USD 3.6647 | wall=0.0 min
[ceninf] corrida completa: gasto global=USD 3.6647 | wall=0.0 min
[ri_rml] corrida completa: gasto global=USD 5.0082 | wall=9.6 min
[nmcief] corrida completa: gasto global=USD 6.7759 | wall=22.8 min
[adrei] corrida completa: gasto global=USD 8.0520 | wall=12.0 min
[opefci] corrida completa: gasto global=USD 9.2290 | wall=11.7 min
[ri_dcpc] corrida completa: gasto global=USD 11.3821 | wall=27.0 min
[snp_tr] corrida completa: gasto global=USD 13.8241 | wall=27.4 min
[efemin] corrida completa: gasto global=USD 16.7676 | wall=31.5 min
[ri_mmsef] corrida completa: gasto global=USD 18.6780 | wall=15.2 min
[manori] corrida completa: gasto global=USD 22.8047 | wall=52.4 min
[expaef] corrida completa: gasto global=USD 25.4397 | wall=23.9 min
[ri_ccna] corrida completa: gasto global=USD 28.9584 | wall=36.8 min
[ayccef] corrida completa: gasto global=USD 32.5915 | wall=35.5 min
[cirmo3] corrida completa: gasto global=USD 37.8783 | wall=56.5 min
[snp_cheq] corrida completa: gasto global=USD 43.9418 | wall=70.5 min
[cajasc] corrida completa: gasto global=USD 49.6757 | wall=60.0 min
[depaho] corrida completa: gasto global=USD 57.9214 | wall=103.6 min
[lingeef] corrida completa: gasto global=USD 70.9910 | wall=159.9 min
```

- **Los 20 tienen sus dos fases cerradas**, cobertura completa (`cob` T), la cobertura exacta de la E0 (`cobE0` T), 0 ids repetidos y 0
  unidades sin destino.
- **El total:** 3.252 aceptadas (los tres estados de aceptación juntos), 42 en cola y 0 errores. 3.252 + 42 + 0 = 3.294, que son las
  unidades con las partes.
- **Las partes por corte:** solo ri_rml tiene, con 50 contra 46 (`ri_rml::Sbloque14` en 5). La corrida en seco preveía también las de
  `snp_cheq::7.2.4` y `lingeef::5.4.2.3`, con la salida p90. En la corrida real, snp_cheq y lingeef no tienen partes (265 y 613): sus
  unidades salieron sin partirse.

## 5. La salida de `conteos_t2.py` y los `NO_ABRIR_`

`.venv/bin/python -B data/experiment/tanda1/t2/conteos_t2.py --repo .` (rc 0):

```
sha256 b0757dc5ad6e0d84701c81977571dc868716a0d2be922d7f9cf2bac468c2dd87
vigilancia integridad_e3: OK
```

El sha256 de los dos `NO_ABRIR_`, que no abrí:

```
99671576331b09ec0258f0adc3a91f4a020f5c18de2062f0667ec6883639903c  data/experiment/tanda1/t2/NO_ABRIR_salida_e3_tanda1.txt
b0757dc5ad6e0d84701c81977571dc868716a0d2be922d7f9cf2bac468c2dd87  data/experiment/tanda1/t2/NO_ABRIR_conteos_reextracciones_tanda1.json
```

## 6. El gasto por TO contra su estimado nuevo

Los gastos son los de las dos fases de cada TO en `estado_corpus.json`: 40 fases cerradas y `fase_actual` en null. El estimado nuevo es el
del manifiesto `818a62cf…`, y el viejo, el de `4dd02505…` (`git show 9d1cdd92:…`), como referencia.

| TO | real USD | estimado nuevo | razón | estimado viejo | razón |
|---|---:|---:|---:|---:|---:|
| ri_gerc | 0,352899 | 0,408570 | 0,8637 | 0,319465 | 1,1047 |
| ri_pgn | 0,796164 | 0,807453 | 0,9860 | 0,447252 | 1,7801 |
| ceninf | 0,808181 | 1,142938 | 0,7071 | 0,823485 | 0,9814 |
| ri_rml | 3,051005 | 3,550498 | 0,8593 | 0,979694 | 3,1142 |
| nmcief | 1,767667 | 2,872825 | 0,6153 | 1,172434 | 1,5077 |
| adrei | 1,276086 | 1,239473 | 1,0295 | 1,478050 | 0,8634 |
| opefci | 1,177010 | 0,588646 | 1,9995 | 1,562510 | 0,7533 |
| ri_dcpc | 2,153094 | 2,154167 | 0,9995 | 1,596739 | 1,3484 |
| snp_tr | 2,442028 | 2,638181 | 0,9256 | 2,194403 | 1,1128 |
| efemin | 2,943467 | 2,527026 | 1,1648 | 2,512685 | 1,1714 |
| ri_mmsef | 1,910386 | 1,730887 | 1,1037 | 2,726105 | 0,7008 |
| manori | 4,126675 | 5,601643 | 0,7367 | 3,236057 | 1,2752 |
| expaef | 2,635037 | 1,437583 | 1,8330 | 3,483975 | 0,7563 |
| ri_ccna | 3,518727 | 3,489889 | 1,0083 | 3,597377 | 0,9781 |
| ayccef | 3,633113 | 2,297370 | 1,5814 | 4,138540 | 0,8779 |
| cirmo3 | 5,286811 | 5,157540 | 1,0251 | 5,405440 | 0,9781 |
| snp_cheq | 6,063496 | 7,586441 | 0,7993 | 5,648652 | 1,0734 |
| cajasc | 5,733857 | 4,646787 | 1,2339 | 6,060005 | 0,9462 |
| depaho | 8,245696 | 5,466447 | 1,5084 | 9,332830 | 0,8835 |
| lingeef | 13,069633 | 14,314829 | 0,9130 | 12,943495 | 1,0097 |
| **total** | **70,991032** | **69,659193** | **1,0191** | **69,659193** | **1,0191** |

- **Contra el estimado de la tanda** (69,6592): USD 1,331839 más, 1,0191 veces.
- **Contra el tope** (100,7291): el 70,48 %, con un margen de USD 29,738068. `presupuesto_compartido.json` da 70,991031 (redondeado a 6
  decimales en cada registro).
- **Por TO, con el estimado nuevo:**
  - las razones van de 0,6153 (nmcief) a 1,9995 (opefci);
  - pasan de 1,5 opefci, expaef (1,8330), ayccef (1,5814) y depaho (1,5084);
  - con el estimado viejo, las de esos cuatro eran de 0,75 a 0,88.
- Las cifras de cierre que usan el desglose de E3 esperan al sello del diseño de U-MED-VERIF (§7).

## 7. La duración contra lo proyectado

- **Los tres lanzamientos** sumaron 813,2 min (13,55 h), a 14,83 s por unidad. La proyección era de unos 649 min, a 11,84 s por unidad,
  con la tasa de la tanda 0: tardó 1,25 veces lo proyectado.
- **El lanzamiento 3 solo** tomó 757,0 min, de las 08:15:22 a las 20:52:20.
- **Los más largos:** lingeef (159,9 min), depaho (103,7) y snp_cheq (70,5).

## 8. La foto del repo, los .pyc y el grep de convenciones

- **Del lanzamiento 3** (`foto_repo_tanda1_t2.py`). Antes: 08:14:57 a 08:15:08, 51.267 entradas. Después: 20:54:00 a 20:54:11, 51.625
  entradas.
  - **359 nuevos:** 358 en `reextraccion_v2/corpus_tanda1/` (45 checkpoints y los archivos de los 17 TOs desde ri_rml) y
    `t2/FRENO_T2_parcial_2.md`, que es el renombre.
  - **1 borrado:** `t2/FRENO_T2.md`, el parcial 2 renombrado.
  - **11 cambiados:**
    - 3 en la salida: `estado_corpus.json`, `presupuesto_compartido.json` y `ultimo_checkpoint.json`;
    - las tres bases, solo por tamaño y fecha: `e1_extraccion.db` de 419.590.144 a 707.031.040 bytes, `e1_reintentos.db` de 54.415.360 a
      74.350.592 y `e3_verificacion.db` de 269.209.600 a 392.163.328;
    - 4 en `t2/`: `avance_t2.jsonl`, `resumen_t2.json` y los dos `NO_ABRIR_`;
    - `logs/cache_usage.jsonl`, solo por tamaño y fecha: de 3.959.624 a 5.455.990.
  - Nada fuera de esas rutas.
- **Desde el inicio de T2** (contra la foto del 16/10 a las 20:47:34):
  - **429 nuevos:** 423 en `corpus_tanda1/` y 6 en `t2/` (`avance_t2.jsonl`, `resumen_t2.json`, los dos `NO_ABRIR_` y los dos parciales
    renombrados).
  - **2 borrados:** el `-shm` y el `-wal` de `e1_extraccion.db`.
  - **8 cambiados:**
    - las tres bases y `logs/cache_usage.jsonl`, que siguen fuera de la lista de lo nuevo del «seguí» (parcial 1, sección 9);
    - los cuatro archivos de `ca5b39fd`: el manifiesto, `t1/sha256_para_T2.txt`, `t2/lanzar_t2.py` y `docs/preregistro_tanda1.md`. Los
      cambió el commit de la autora, no la corrida: `git diff --stat ea61cfdb HEAD` da esos cuatro archivos, y
      `git status --porcelain --untracked-files=no` sigue vacío.
  - **En `t2/`, además, respecto de HEAD:** `foto_repo_tanda1_t2.py`, escrito antes de la primera foto, y este FRENO, escrito después de la
    última.
- **Los `.pyc`:** 11.236 al inicio de T2 y 11.236 al final, iguales (`diff` vacío).
- **El grep de convenciones**, sobre lo nuevo de `t2/` sin los `NO_ABRIR_`. El resultado, con el control positivo, va en el mensaje del FRENO.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. No hice ninguna copia del repo.
- **Lo que miré en disco:**
  - durante la corrida, solo `avance_t2.jsonl`;
  - después, las fotos (bases y log de uso por tamaño) y, de `estado_corpus.json`, solo los gastos y los nombres de las fases.
  - Ningún `ls` de las carpetas de salida.

## 9. Errores propios

1. **El gasto de la tabla de la sección 3, completado a mano.** En la primera redacción de este FRENO, desde ri_rml del lanzamiento 3,
   escribí el gasto global a mano, completando con ceros las cifras de 4 decimales de la salida de `tabla_avance_t2.py`. En ri_rml puse
   5,008156, que no sale de ningún archivo: el renglón dice 5,008249.
   - La causa: armé esa parte de la tabla a mano, en lugar de generarla del registro.
   - Lo detecté al releer, antes de entregar. Regeneré la tabla entera por script desde `avance_t2.jsonl`.
   - Volví a controlar el 1,957244 de ceninf que cité en el parcial 2: es el de su renglón.
2. Los errores del lanzamiento 1 están declarados en el parcial 1: el archivo en `/tmp` y el `ls` de la salida de ri_pgn. El parcial 2 no
   tuvo ninguno.

## 10. Para la autora

1. **La extracción de la tanda 1 está completa**, dentro del tope. Lo que sigue, del §5 (cierre, sellos y mediciones), no lo hice: no era
   de este «seguí».
2. **El estimado por caracteres** acertó el total (1,0191 veces), y por TO se desvió como muestra la sección 6. Es un insumo para el
   re-presupuesto de la tanda 2 (§3, «Al cerrar»).
3. **La corrida en seco preveía partes en snp_cheq y lingeef** con la salida p90, y la corrida real no las tuvo (sección 4). La salida por
   carácter real de esas unidades quedó por debajo de la p90.
4. **La duración** fue 1,25 veces la proyectada (sección 7).
5. **Siguen** la doble cuenta de la fase que cierra en la proyección (parcial 1, sección 5) y `logs/cache_usage.jsonl` fuera de la lista del
   «seguí».

FRENO T2. Espero la revisión de la autora.
