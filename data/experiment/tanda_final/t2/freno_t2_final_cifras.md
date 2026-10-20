# Cifras del FRENO T2 final de la tanda final (las genera freno_t2_final_cifras.py)

### 1. Los lanzamientos

| # | inicio | pid | fin | minutos | salida | opciones | controles previos | freno antes | parada | copia de trabajo borrada |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19T00:08:43-0300 | 39763 | 2026-10-19T02:35:20-0300 | 146.6 | rc=11 | autorizado_tramo_2=False, retomar_tras_pausa=False, stub=False | True (HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 True; tope True) | OK [] [] | FRENO del control entre tramos: decide la autora | True |
| 2 | 2026-10-19T08:42:24-0300 | 70654 | 2026-10-20T00:11:16-0300 | 928.9 | rc=0 | autorizado_tramo_2=True, retomar_tras_pausa=False, stub=False | True (HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 True; tope True) | OK ['claude-haiku-4-5-20251001'] ['claude-sonnet-5'] | — | True |

### 2. Por TO, del registro de avance: los 98 que corrieron

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

### 3. Los controles entre tramos

| lanz. | hora | rc | resultado | salida | control sha256 |
|---|---|---|---|---|---|
| 1 | 2026-10-19T02:35:20-0300 | 3 | FRENO | OK    costo por unidad: 0.021391 (umbral 0.03423) / OK    salidas inválidas de E1: 0.001664 (umbral 0.01) / FRENO errores definitivos: 1 (umbral 0) / OK    proporción a la cola: 0.021631 (umbral 0.030109) / info  reintento por forma de E1: 6 de 601 unidades (sin umbral) | ca5f9b7bb363… |
| 2 | 2026-10-19T08:43:31-0300 | 3 | FRENO | OK    costo por unidad: 0.021391 (umbral 0.03423) / OK    salidas inválidas de E1: 0.001664 (umbral 0.01) / FRENO errores definitivos: 1 (umbral 0) / OK    proporción a la cola: 0.021631 (umbral 0.030109) / info  reintento por forma de E1: 6 de 601 unidades (sin umbral) | ca5f9b7bb363… |

### 4. resumen_t2.py por TO

| TO | tramo | unidades | unidades_con_partes | aceptadas | cola | errores | sin_destino | ids_repetidos | cobertura | cobertura E0 | fases cerradas | gasto USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ri_bdp | tramo 1 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | True | True | True | 0.116308 |
| ri_ieccm | tramo 1 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | True | True | True | 0.057636 |
| ri_rcl | tramo 1 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | True | True | True | 0.073994 |
| ri_esd | tramo 1 | 5 | 5 | 5 | 0 | 0 | 0 | 0 | True | True | True | 0.089149 |
| verac | tramo 1 | 5 | 5 | 5 | 0 | 0 | 0 | 0 | True | True | True | 0.106223 |
| ri_acsf | tramo 1 | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.093206 |
| ri_cr | tramo 1 | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.201477 |
| ri_tvf | tramo 1 | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.144593 |
| ribspc | tramo 1 | 7 | 7 | 7 | 0 | 0 | 0 | 0 | True | True | True | 0.07889 |
| asomut | tramo 1 | 8 | 8 | 8 | 0 | 0 | 0 | 0 | True | True | True | 0.136145 |
| micemp | tramo 1 | 8 | 8 | 8 | 0 | 0 | 0 | 0 | True | True | True | 0.135159 |
| ri_psp | tramo 1 | 9 | 9 | 9 | 0 | 0 | 0 | 0 | True | True | True | 0.359484 |
| ri_transpa | tramo 1 | 11 | 11 | 10 | 0 | 1 | 0 | 0 | True | True | True | 0.481275 |
| ri_iesinap | tramo 1 | 12 | 12 | 12 | 0 | 0 | 0 | 0 | True | True | True | 0.2316 |
| ri_msrl | tramo 1 | 12 | 12 | 10 | 2 | 0 | 0 | 0 | True | True | True | 0.503968 |
| ri_iepsp | tramo 1 | 13 | 13 | 12 | 1 | 0 | 0 | 0 | True | True | True | 0.428729 |
| ri_ai | tramo 1 | 15 | 15 | 15 | 0 | 0 | 0 | 0 | True | True | True | 0.316697 |
| ri_pspapt | tramo 1 | 16 | 16 | 16 | 0 | 0 | 0 | 0 | True | True | True | 0.284352 |
| ri_tsa | tramo 1 | 17 | 17 | 17 | 0 | 0 | 0 | 0 | True | True | True | 0.760313 |
| ri_tar | tramo 1 | 18 | 18 | 17 | 1 | 0 | 0 | 0 | True | True | True | 0.269103 |
| ri_laft | tramo 1 | 26 | 26 | 26 | 0 | 0 | 0 | 0 | True | True | True | 0.711444 |
| ri_dsf | tramo 1 | 28 | 28 | 26 | 2 | 0 | 0 | 0 | True | True | True | 0.80593 |
| ri_nge | tramo 1 | 30 | 30 | 30 | 0 | 0 | 0 | 0 | True | True | True | 0.284692 |
| ri_ot | tramo 1 | 32 | 32 | 32 | 0 | 0 | 0 | 0 | True | True | True | 0.409084 |
| consyr | tramo 1 | 34 | 34 | 32 | 2 | 0 | 0 | 0 | True | True | True | 0.560574 |
| ri_secoexpo | tramo 1 | 35 | 35 | 34 | 1 | 0 | 0 | 0 | True | True | True | 0.907826 |
| seggar | tramo 1 | 36 | 36 | 34 | 2 | 0 | 0 | 0 | True | True | True | 0.924249 |
| ri_sef | tramo 1 | 38 | 38 | 38 | 0 | 0 | 0 | 0 | True | True | True | 0.736113 |
| cedin | tramo 1 | 66 | 66 | 65 | 1 | 0 | 0 | 0 | True | True | True | 1.249616 |
| ri_ii_31_12_19 | tramo 1 | 91 | 91 | 90 | 1 | 0 | 0 | 0 | True | True | True | 1.39836 |
| reqcac | tramo 2 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | True | True | True | 0.313149 |
| cateloc | tramo 2 | 11 | 11 | 8 | 3 | 0 | 0 | 0 | True | True | True | 1.011697 |
| convca | tramo 2 | 12 | 12 | 12 | 0 | 0 | 0 | 0 | True | True | True | 0.225904 |
| socgar | tramo 2 | 12 | 12 | 12 | 0 | 0 | 0 | 0 | True | True | True | 0.239236 |
| horari | tramo 2 | 13 | 13 | 13 | 0 | 0 | 0 | 0 | True | True | True | 0.270246 |
| osapsa | tramo 2 | 13 | 13 | 13 | 0 | 0 | 0 | 0 | True | True | True | 0.276032 |
| snp_atm | tramo 2 | 16 | 16 | 16 | 0 | 0 | 0 | 0 | True | True | True | 0.242324 |
| pognme | tramo 2 | 17 | 17 | 17 | 0 | 0 | 0 | 0 | True | True | True | 0.328857 |
| evacre | tramo 2 | 19 | 19 | 18 | 1 | 0 | 0 | 0 | True | True | True | 0.344512 |
| regpri | tramo 2 | 20 | 20 | 16 | 4 | 0 | 0 | 0 | True | True | True | 0.390305 |
| cescar | tramo 2 | 21 | 21 | 19 | 2 | 0 | 0 | 0 | True | True | True | 0.488909 |
| ctacor | tramo 2 | 21 | 21 | 21 | 0 | 0 | 0 | 0 | True | True | True | 0.442224 |
| fgarcp | tramo 2 | 22 | 22 | 22 | 0 | 0 | 0 | 0 | True | True | True | 0.459993 |
| pscpp | tramo 2 | 22 | 22 | 22 | 0 | 0 | 0 | 0 | True | True | True | 0.399688 |
| secfin | tramo 2 | 22 | 22 | 20 | 2 | 0 | 0 | 0 | True | True | True | 0.37923 |
| incuca | tramo 2 | 23 | 23 | 23 | 0 | 0 | 0 | 0 | True | True | True | 0.381916 |
| venliq | tramo 2 | 23 | 23 | 23 | 0 | 0 | 0 | 0 | True | True | True | 0.474096 |
| fclef | tramo 2 | 28 | 28 | 28 | 0 | 0 | 0 | 0 | True | True | True | 0.420158 |
| lavdin | tramo 2 | 29 | 29 | 28 | 1 | 0 | 0 | 0 | True | True | True | 0.521095 |
| rmrtsd | tramo 2 | 31 | 31 | 31 | 0 | 0 | 0 | 0 | True | True | True | 0.798601 |
| ccbcra | tramo 2 | 32 | 32 | 32 | 0 | 0 | 0 | 0 | True | True | True | 0.510589 |
| apnf | tramo 2 | 34 | 34 | 33 | 1 | 0 | 0 | 0 | True | True | True | 0.622244 |
| traval | tramo 2 | 35 | 35 | 34 | 1 | 0 | 0 | 0 | True | True | True | 0.787142 |
| disres | tramo 2 | 38 | 38 | 35 | 3 | 0 | 0 | 0 | True | True | True | 0.960518 |
| relact | tramo 2 | 38 | 38 | 38 | 0 | 0 | 0 | 0 | True | True | True | 0.599037 |
| coltit | tramo 2 | 39 | 39 | 39 | 0 | 0 | 0 | 0 | True | True | True | 0.555115 |
| raapal | tramo 2 | 40 | 40 | 38 | 2 | 0 | 0 | 0 | True | True | True | 1.140939 |
| servco | tramo 2 | 40 | 40 | 39 | 1 | 0 | 0 | 0 | True | True | True | 0.765909 |
| retype | tramo 2 | 41 | 41 | 40 | 1 | 0 | 0 | 0 | True | True | True | 0.55196 |
| fabcra | tramo 2 | 42 | 42 | 40 | 2 | 0 | 0 | 0 | True | True | True | 0.82789 |
| ri2_ci | tramo 2 | 45 | 45 | 45 | 0 | 0 | 0 | 0 | True | True | True | 1.226355 |
| icmecma | tramo 2 | 48 | 48 | 48 | 0 | 0 | 0 | 0 | True | True | True | 1.008334 |
| pfmipyme | tramo 2 | 52 | 52 | 52 | 0 | 0 | 0 | 0 | True | True | True | 0.740373 |
| prevmi | tramo 2 | 52 | 52 | 51 | 1 | 0 | 0 | 0 | True | True | True | 1.270419 |
| fimipyme | tramo 2 | 55 | 55 | 53 | 2 | 0 | 0 | 0 | True | True | True | 1.118683 |
| garopt | tramo 2 | 55 | 55 | 54 | 1 | 0 | 0 | 0 | True | True | True | 0.819326 |
| actgar | tramo 2 | 60 | 60 | 60 | 0 | 0 | 0 | 0 | True | True | True | 1.046085 |
| gescre | tramo 2 | 61 | 61 | 60 | 1 | 0 | 0 | 0 | True | True | True | 1.277993 |
| snp_mep | tramo 2 | 62 | 62 | 62 | 0 | 0 | 0 | 0 | True | True | True | 1.456688 |
| opecam | tramo 2 | 65 | 65 | 65 | 0 | 0 | 0 | 0 | True | True | True | 1.277091 |
| ordcom | tramo 2 | 65 | 65 | 65 | 0 | 0 | 0 | 0 | True | True | True | 0.994026 |
| gracre | tramo 2 | 67 | 67 | 66 | 1 | 0 | 0 | 0 | True | True | True | 1.270727 |
| supcon | tramo 2 | 67 | 67 | 67 | 0 | 0 | 0 | 0 | True | True | True | 1.209209 |
| cryl | tramo 2 | 68 | 68 | 67 | 1 | 0 | 0 | 0 | True | True | True | 1.299741 |
| tasint | tramo 2 | 69 | 69 | 68 | 1 | 0 | 0 | 0 | True | True | True | 1.268551 |
| snp_debin | tramo 2 | 71 | 71 | 71 | 0 | 0 | 0 | 0 | True | True | True | 1.189624 |
| afiltr | tramo 2 | 72 | 72 | 71 | 1 | 0 | 0 | 0 | True | True | True | 1.907851 |
| autenf | tramo 2 | 75 | 75 | 72 | 3 | 0 | 0 | 0 | True | True | True | 1.460454 |
| rrci | tramo 2 | 77 | 77 | 77 | 0 | 0 | 0 | 0 | True | True | True | 1.427976 |
| rmgcti | tramo 2 | 81 | 81 | 80 | 1 | 0 | 0 | 0 | True | True | True | 2.602919 |
| repefe | tramo 2 | 87 | 87 | 86 | 1 | 0 | 0 | 0 | True | True | True | 1.41913 |
| snp_psp | tramo 2 | 89 | 89 | 89 | 0 | 0 | 0 | 0 | True | True | True | 1.701944 |
| jafip | tramo 2 | 91 | 91 | 89 | 2 | 0 | 0 | 0 | True | True | True | 1.713857 |
| inspag | tramo 2 | 93 | 93 | 93 | 0 | 0 | 0 | 0 | True | True | True | 1.681341 |
| graloc | tramo 2 | 100 | 100 | 99 | 1 | 0 | 0 | 0 | True | True | True | 2.034889 |
| adfsp | tramo 2 | 101 | 101 | 100 | 1 | 0 | 0 | 0 | True | True | True | 1.881406 |
| seguef | tramo 2 | 101 | 101 | 101 | 0 | 0 | 0 | 0 | True | True | True | 1.896696 |
| garant | tramo 2 | 106 | 106 | 106 | 0 | 0 | 0 | 0 | True | True | True | 1.93256 |
| snp_cec | tramo 2 | 122 | 122 | 119 | 3 | 0 | 0 | 0 | True | True | True | 2.303711 |
| snp_spd | tramo 2 | 130 | 130 | 129 | 1 | 0 | 0 | 0 | True | True | True | 2.283119 |
| snp_dd | tramo 2 | 131 | 131 | 131 | 0 | 0 | 0 | 0 | True | True | True | 2.398987 |
| ratio | tramo 2 | 133 | 133 | 128 | 5 | 0 | 0 | 0 | True | True | True | 2.808285 |
| ratiofn | tramo 2 | 133 | 133 | 130 | 3 | 0 | 0 | 0 | True | True | True | 2.630161 |
| finsec | tramo 2 | 134 | 134 | 128 | 6 | 0 | 0 | 0 | True | True | True | 3.043122 |
| snp_tr_nc | tramo 2 | 136 | 136 | 136 | 0 | 0 | 0 | 0 | True | True | True | 2.334208 |
| pimf | tramo 2 | 165 | 165 | 164 | 1 | 0 | 0 | 0 | True | True | True | 2.978591 |
| depinv | tramo 2 | 203 | 203 | 201 | 2 | 0 | 0 | 0 | True | True | True | 3.225965 |
| ctavis | tramo 2 | 271 | 271 | 267 | 4 | 0 | 0 | 0 | True | True | True | 4.872242 |
| total del tramo 1 |  | 601 | 601 | 587 | 13 | 1 | 0 | 0 |  |  |  | 12.856189 |
| total del tramo 2 |  | 4350 | 4350 | 4283 | 67 | 0 | 0 | 0 |  |  |  | 84.742154 |
| total |  | 4951 | 4951 | 4870 | 80 | 1 | 0 | 0 |  |  | 98 | 97.598343 |

### 5. El costo por TO: real contra el §3 más las líneas de alcance y contra el repartido

| TO | tramo | gasto real | §3 + líneas | real / §3 | repartido | real / repartido |
|---|---|---|---|---|---|---|
| ri_bdp | tramo 1 | 0.116308 | 0.063893 | 1.8204 | 0.063716 | 1.8254 |
| ri_ieccm | tramo 1 | 0.057636 | 0.085155 | 0.6768 | 0.019651 | 2.9330 |
| ri_rcl | tramo 1 | 0.073994 | 0.085191 | 0.8686 | 0.071423 | 1.0360 |
| ri_esd | tramo 1 | 0.089149 | 0.106488 | 0.8372 | 0.177690 | 0.5017 |
| verac | tramo 1 | 0.106223 | 0.106449 | 0.9979 | 0.047864 | 2.2193 |
| ri_acsf | tramo 1 | 0.093206 | 0.127786 | 0.7294 | 0.084970 | 1.0969 |
| ri_cr | tramo 1 | 0.201477 | 0.126690 | 1.5903 | 0.143856 | 1.4005 |
| ri_tvf | tramo 1 | 0.144593 | 0.127786 | 1.1315 | 0.200986 | 0.7194 |
| ribspc | tramo 1 | 0.078890 | 0.149084 | 0.5292 | 0.026852 | 2.9380 |
| asomut | tramo 1 | 0.136145 | 0.168920 | 0.8060 | 0.087100 | 1.5631 |
| micemp | tramo 1 | 0.135159 | 0.168920 | 0.8001 | 0.092545 | 1.4605 |
| ri_psp | tramo 1 | 0.359484 | 0.191670 | 1.8755 | 1.662599 | 0.2162 |
| ri_transpa | tramo 1 | 0.481275 | 0.232265 | 2.0721 | 1.602220 | 0.3004 |
| ri_iesinap | tramo 1 | 0.231600 | 0.253380 | 0.9140 | 0.311446 | 0.7436 |
| ri_msrl | tramo 1 | 0.503968 | 0.255572 | 1.9719 | 0.640304 | 0.7871 |
| ri_iepsp | tramo 1 | 0.428729 | 0.277371 | 1.5457 | 0.541524 | 0.7917 |
| ri_ai | tramo 1 | 0.316697 | 0.319465 | 0.9913 | 0.282838 | 1.1197 |
| ri_pspapt | tramo 1 | 0.284352 | 0.337840 | 0.8417 | 0.231131 | 1.2303 |
| ri_tsa | tramo 1 | 0.760313 | 0.361927 | 2.1007 | 1.184836 | 0.6417 |
| ri_tar | tramo 1 | 0.269103 | 0.383358 | 0.7020 | 0.217233 | 1.2388 |
| ri_laft | tramo 1 | 0.711444 | 0.548990 | 1.2959 | 1.369816 | 0.5194 |
| ri_dsf | tramo 1 | 0.805930 | 0.591220 | 1.3632 | 1.292377 | 0.6236 |
| ri_nge | tramo 1 | 0.284692 | 0.638931 | 0.4456 | 0.069886 | 4.0737 |
| ri_ot | tramo 1 | 0.409084 | 0.681526 | 0.6002 | 0.975397 | 0.4194 |
| consyr | tramo 1 | 0.560574 | 0.723855 | 0.7744 | 0.415628 | 1.3487 |
| ri_secoexpo | tramo 1 | 0.907826 | 0.745419 | 1.2179 | 1.845976 | 0.4918 |
| seggar | tramo 1 | 0.924249 | 0.766435 | 1.2059 | 0.857318 | 1.0781 |
| ri_sef | tramo 1 | 0.736113 | 0.809312 | 0.9096 | 1.206024 | 0.6104 |
| cedin | tramo 1 | 1.249616 | 1.405130 | 0.8893 | 1.112074 | 1.1237 |
| ri_ii_31_12_19 | tramo 1 | 1.398360 | 1.938566 | 0.7213 | 2.474732 | 0.5651 |
| reqcac | tramo 2 | 0.313149 | 0.063897 | 4.9008 | 0.435784 | 0.7186 |
| cateloc | tramo 2 | 1.011697 | 0.234188 | 4.3200 | 3.912391 | 0.2586 |
| convca | tramo 2 | 0.225904 | 0.253380 | 0.8916 | 0.172553 | 1.3092 |
| socgar | tramo 2 | 0.239236 | 0.253380 | 0.9442 | 0.167217 | 1.4307 |
| horari | tramo 2 | 0.270246 | 0.276768 | 0.9764 | 0.358454 | 0.7539 |
| osapsa | tramo 2 | 0.276032 | 0.274495 | 1.0056 | 0.206123 | 1.3392 |
| snp_atm | tramo 2 | 0.242324 | 0.337840 | 0.7173 | 0.171784 | 1.4106 |
| pognme | tramo 2 | 0.328857 | 0.358955 | 0.9162 | 0.232251 | 1.4160 |
| evacre | tramo 2 | 0.344512 | 0.401185 | 0.8587 | 0.226630 | 1.5202 |
| regpri | tramo 2 | 0.390305 | 0.422300 | 0.9242 | 0.280993 | 1.3890 |
| cescar | tramo 2 | 0.488909 | 0.443415 | 1.1026 | 0.274780 | 1.7793 |
| ctacor | tramo 2 | 0.442224 | 0.443415 | 0.9973 | 0.611651 | 0.7230 |
| fgarcp | tramo 2 | 0.459993 | 0.464530 | 0.9902 | 0.446762 | 1.0296 |
| pscpp | tramo 2 | 0.399688 | 0.464530 | 0.8604 | 0.339045 | 1.1789 |
| secfin | tramo 2 | 0.379230 | 0.464530 | 0.8164 | 0.300161 | 1.2634 |
| incuca | tramo 2 | 0.381916 | 0.485645 | 0.7864 | 0.280576 | 1.3612 |
| venliq | tramo 2 | 0.474096 | 0.489667 | 0.9682 | 0.340582 | 1.3920 |
| fclef | tramo 2 | 0.420158 | 0.591220 | 0.7107 | 0.287449 | 1.4617 |
| lavdin | tramo 2 | 0.521095 | 0.612335 | 0.8510 | 0.353295 | 1.4750 |
| rmrtsd | tramo 2 | 0.798601 | 0.654565 | 1.2200 | 1.214696 | 0.6574 |
| ccbcra | tramo 2 | 0.510589 | 0.675680 | 0.7557 | 0.317440 | 1.6085 |
| apnf | tramo 2 | 0.622244 | 0.717910 | 0.8667 | 0.755376 | 0.8238 |
| traval | tramo 2 | 0.787142 | 0.739025 | 1.0651 | 0.767386 | 1.0257 |
| disres | tramo 2 | 0.960518 | 0.802370 | 1.1971 | 1.087988 | 0.8828 |
| relact | tramo 2 | 0.599037 | 0.802370 | 0.7466 | 0.354327 | 1.6906 |
| coltit | tramo 2 | 0.555115 | 0.823485 | 0.6741 | 0.275636 | 2.0139 |
| raapal | tramo 2 | 1.140939 | 0.844600 | 1.3509 | 1.655442 | 0.6892 |
| servco | tramo 2 | 0.765909 | 0.844600 | 0.9068 | 0.511598 | 1.4971 |
| retype | tramo 2 | 0.551960 | 0.865715 | 0.6376 | 0.322512 | 1.7114 |
| fabcra | tramo 2 | 0.827890 | 0.886830 | 0.9335 | 1.106541 | 0.7482 |
| ri2_ci | tramo 2 | 1.226355 | 0.950175 | 1.2907 | 1.924359 | 0.6373 |
| icmecma | tramo 2 | 1.008334 | 1.013520 | 0.9949 | 0.775422 | 1.3004 |
| pfmipyme | tramo 2 | 0.740373 | 1.097980 | 0.6743 | 0.537572 | 1.3773 |
| prevmi | tramo 2 | 1.270419 | 1.097980 | 1.1571 | 0.965583 | 1.3157 |
| fimipyme | tramo 2 | 1.118683 | 1.161325 | 0.9633 | 0.745869 | 1.4998 |
| garopt | tramo 2 | 0.819326 | 1.170942 | 0.6997 | 0.385680 | 2.1244 |
| actgar | tramo 2 | 1.046085 | 1.266900 | 0.8257 | 0.551338 | 1.8974 |
| gescre | tramo 2 | 1.277993 | 1.288015 | 0.9922 | 1.220405 | 1.0472 |
| snp_mep | tramo 2 | 1.456688 | 1.309130 | 1.1127 | 2.215958 | 0.6574 |
| opecam | tramo 2 | 1.277091 | 1.383776 | 0.9229 | 1.155876 | 1.1049 |
| ordcom | tramo 2 | 0.994026 | 1.372475 | 0.7243 | 0.664587 | 1.4957 |
| gracre | tramo 2 | 1.270727 | 1.414705 | 0.8982 | 0.707995 | 1.7948 |
| supcon | tramo 2 | 1.209209 | 1.414705 | 0.8547 | 0.958118 | 1.2621 |
| cryl | tramo 2 | 1.299741 | 1.435820 | 0.9052 | 1.128980 | 1.1513 |
| tasint | tramo 2 | 1.268551 | 1.456935 | 0.8707 | 0.942046 | 1.3466 |
| snp_debin | tramo 2 | 1.189624 | 1.499165 | 0.7935 | 0.868010 | 1.3705 |
| afiltr | tramo 2 | 1.907851 | 1.520280 | 1.2549 | 2.977481 | 0.6408 |
| autenf | tramo 2 | 1.460454 | 1.583625 | 0.9222 | 1.413508 | 1.0332 |
| rrci | tramo 2 | 1.427976 | 1.625855 | 0.8783 | 1.766957 | 0.8082 |
| rmgcti | tramo 2 | 2.602919 | 1.710315 | 1.5219 | 3.898339 | 0.6677 |
| repefe | tramo 2 | 1.419130 | 1.837005 | 0.7725 | 1.308163 | 1.0848 |
| snp_psp | tramo 2 | 1.701944 | 1.879235 | 0.9057 | 1.445213 | 1.1776 |
| jafip | tramo 2 | 1.713857 | 1.937376 | 0.8846 | 1.297800 | 1.3206 |
| inspag | tramo 2 | 1.681341 | 1.979956 | 0.8492 | 2.042988 | 0.8230 |
| graloc | tramo 2 | 2.034889 | 2.111500 | 0.9637 | 1.973563 | 1.0311 |
| adfsp | tramo 2 | 1.881406 | 2.132615 | 0.8822 | 2.231107 | 0.8433 |
| seguef | tramo 2 | 1.896696 | 2.150275 | 0.8821 | 1.722056 | 1.1014 |
| garant | tramo 2 | 1.932560 | 2.256724 | 0.8564 | 2.266457 | 0.8527 |
| snp_cec | tramo 2 | 2.303711 | 2.576030 | 0.8943 | 2.449987 | 0.9403 |
| snp_spd | tramo 2 | 2.283119 | 2.744950 | 0.8318 | 1.711342 | 1.3341 |
| snp_dd | tramo 2 | 2.398987 | 2.788970 | 0.8602 | 3.853900 | 0.6225 |
| ratio | tramo 2 | 2.808285 | 2.808295 | 1.0000 | 4.258373 | 0.6595 |
| ratiofn | tramo 2 | 2.630161 | 2.808295 | 0.9366 | 1.546869 | 1.7003 |
| finsec | tramo 2 | 3.043122 | 2.829410 | 1.0755 | 3.848192 | 0.7908 |
| snp_tr_nc | tramo 2 | 2.334208 | 2.871640 | 0.8128 | 1.607578 | 1.4520 |
| pimf | tramo 2 | 2.978591 | 3.483975 | 0.8549 | 2.420324 | 1.2307 |
| depinv | tramo 2 | 3.225965 | 4.286345 | 0.7526 | 2.202301 | 1.4648 |
| ctavis | tramo 2 | 4.872242 | 5.722165 | 0.8515 | 3.682072 | 1.3232 |

### 6. El costo por tramo y total (el §3 del pre-registro va redondeado a cuatro decimales; las líneas de A3 se restan de U × tarifa exacto)

|  | gasto real | §3 del pre-registro | U × tarifa | líneas de A3 | §3 + líneas | real / (§3 + líneas) | repartido | real / repartido |
|---|---|---|---|---|---|---|---|---|
| tramo 1 | 12.856189 | 12.6901 | 12.690115 | 0.088479 | 12.778594 | 1.0061 | 19.310012 | 0.6658 |
| tramo 2 | 84.742154 | 91.8502 | 91.850250 | 0.120959 | 91.971209 | 0.9214 | 85.439791 | 0.9918 |
| total | 97.598343 | 104.5404 | 104.540365 | 0.209438 | 104.749803 | 0.9317 | 104.749803 | 0.9317 |

Contra el tope de USD 151.5835: 0.6439 del tope, con un margen de 53.985157. El gasto por TO sumado da 97.598343 y el global del runner, 97.598343.

Por TO, real / (§3 + líneas): de ('ri_nge', Decimal('0.4456')) a ('reqcac', Decimal('4.9008')); real / repartido: de ('ri_psp', Decimal('0.2162')) a ('ri_nge', Decimal('4.0737')).

### 7. La duración

|  | real (min) | proyectado por unidades (min) | proyectado por caracteres (min) |
|---|---|---|---|
| tramo 1 (suma de sus TOs, lanzamiento 1) | 146.7 | 148.6 | 183.5 |
| tramo 2 (suma de sus TOs, lanzamiento 2) | 927.9 | 1075.3 | 812.0 |
| los dos lanzamientos, de inicio a fin | [146.6, 928.9] → 1075.5 | 1223.8 | 995.5 |

Entre el fin del lanzamiento 1 (2026-10-19T02:35:20-0300) y el inicio del 2 (2026-10-19T08:42:24-0300): 6 h 7 min 4 s, que no cuentan. La pasada del lanzamiento 2 por el tramo 1: 1.05 min.

### 8. La foto del repo: antes, después y lo que cambia

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

### 8b. Los commits de la autora durante T2

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
