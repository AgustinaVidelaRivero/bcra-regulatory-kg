# Cifras del FRENO T2 de la tanda final (las genera freno_t2_cifras.py)

### 1. Los lanzamientos

| # | inicio | pid | fin | minutos | copia de trabajo borrada | salida | parada |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19T00:08:43-0300 | 39763 | 2026-10-19T02:35:20-0300 | 146.6 | True | rc=11 | FRENO del control entre tramos: decide la autora |

Controles previos: ok=True; 161552636 KB libres; HEAD:  78 de 78, árbol: 78 de 78; SDK 0.100.0; sha256 del manifiesto True; tope True; tramos True. Freno por modelo antes del primer TO, sobre 98 TOs: OK (ids de E1 [], de E3 []).

### 2. Por TO, del registro de avance

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

### 3. El control entre tramos

| criterio | valor | umbral | resultado |
|---|---|---|---|
| costo por unidad | 0.021391 | 0.03423 | OK |
| salidas inválidas de E1 | 0.001664 | 0.01 | OK |
| errores definitivos | 1 | 0 | FRENO |
| proporción a la cola | 0.021631 | 0.030109 | OK |

Medido: {"tos": 30, "fases_cerradas": true, "unidades": 601, "gasto_usd": 12.856189, "errores": 1, "cola": 13, "salidas_invalidas_e1": 1, "reintento_por_forma_e1_informacion": 6}.

### 4. resumen_t2.py, el tramo 1 por TO

| TO | unidades | unidades_con_partes | aceptadas | cola | errores | sin_destino | ids_repetidos | cobertura | cobertura E0 | fases cerradas | gasto USD |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ri_bdp | 3 | 3 | 3 | 0 | 0 | 0 | 0 | True | True | True | 0.116308 |
| ri_ieccm | 4 | 4 | 4 | 0 | 0 | 0 | 0 | True | True | True | 0.057636 |
| ri_rcl | 4 | 4 | 4 | 0 | 0 | 0 | 0 | True | True | True | 0.073994 |
| ri_esd | 5 | 5 | 5 | 0 | 0 | 0 | 0 | True | True | True | 0.089149 |
| verac | 5 | 5 | 5 | 0 | 0 | 0 | 0 | True | True | True | 0.106223 |
| ri_acsf | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.093206 |
| ri_cr | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.201477 |
| ri_tvf | 6 | 6 | 6 | 0 | 0 | 0 | 0 | True | True | True | 0.144593 |
| ribspc | 7 | 7 | 7 | 0 | 0 | 0 | 0 | True | True | True | 0.07889 |
| asomut | 8 | 8 | 8 | 0 | 0 | 0 | 0 | True | True | True | 0.136145 |
| micemp | 8 | 8 | 8 | 0 | 0 | 0 | 0 | True | True | True | 0.135159 |
| ri_psp | 9 | 9 | 9 | 0 | 0 | 0 | 0 | True | True | True | 0.359484 |
| ri_transpa | 11 | 11 | 10 | 0 | 1 | 0 | 0 | True | True | True | 0.481275 |
| ri_iesinap | 12 | 12 | 12 | 0 | 0 | 0 | 0 | True | True | True | 0.2316 |
| ri_msrl | 12 | 12 | 10 | 2 | 0 | 0 | 0 | True | True | True | 0.503968 |
| ri_iepsp | 13 | 13 | 12 | 1 | 0 | 0 | 0 | True | True | True | 0.428729 |
| ri_ai | 15 | 15 | 15 | 0 | 0 | 0 | 0 | True | True | True | 0.316697 |
| ri_pspapt | 16 | 16 | 16 | 0 | 0 | 0 | 0 | True | True | True | 0.284352 |
| ri_tsa | 17 | 17 | 17 | 0 | 0 | 0 | 0 | True | True | True | 0.760313 |
| ri_tar | 18 | 18 | 17 | 1 | 0 | 0 | 0 | True | True | True | 0.269103 |
| ri_laft | 26 | 26 | 26 | 0 | 0 | 0 | 0 | True | True | True | 0.711444 |
| ri_dsf | 28 | 28 | 26 | 2 | 0 | 0 | 0 | True | True | True | 0.80593 |
| ri_nge | 30 | 30 | 30 | 0 | 0 | 0 | 0 | True | True | True | 0.284692 |
| ri_ot | 32 | 32 | 32 | 0 | 0 | 0 | 0 | True | True | True | 0.409084 |
| consyr | 34 | 34 | 32 | 2 | 0 | 0 | 0 | True | True | True | 0.560574 |
| ri_secoexpo | 35 | 35 | 34 | 1 | 0 | 0 | 0 | True | True | True | 0.907826 |
| seggar | 36 | 36 | 34 | 2 | 0 | 0 | 0 | True | True | True | 0.924249 |
| ri_sef | 38 | 38 | 38 | 0 | 0 | 0 | 0 | True | True | True | 0.736113 |
| cedin | 66 | 66 | 65 | 1 | 0 | 0 | 0 | True | True | True | 1.249616 |
| ri_ii_31_12_19 | 91 | 91 | 90 | 1 | 0 | 0 | 0 | True | True | True | 1.39836 |
| total del tramo 1 | 601 | 601 | 587 | 13 | 1 | 0 | 0 |  |  | 30 | 12.856189 |

Total de resumen_t2 (los 98): {"unidades": 4951, "unidades_con_partes": 4951, "aceptadas": 587, "cola": 13, "errores": 1, "estado_fuera_del_vocabulario": 0, "sin_destino": 4350, "ids_repetidos": 0, "gasto_por_to_sumado_usd": 12.856189, "tos_cerrados": 30}; gasto global USD 12.856189 de un tope de 151.5835 (dentro: True). Los 68 del tramo 2: con alguna fase o gasto, 0. Líneas del runner que toma resumen_t2: {'corrida completa': 30}.

### 5. El costo del tramo 1 por TO: real contra el estimado del §3 (tarifa más líneas de alcance) y contra el repartido

| TO | gasto real | §3 + líneas | real / §3 | repartido | real / repartido |
|---|---|---|---|---|---|
| ri_bdp | 0.116308 | 0.063893 | 1.8204 | 0.063716 | 1.8254 |
| ri_ieccm | 0.057636 | 0.085155 | 0.6768 | 0.019651 | 2.9330 |
| ri_rcl | 0.073994 | 0.085191 | 0.8686 | 0.071423 | 1.0360 |
| ri_esd | 0.089149 | 0.106488 | 0.8372 | 0.177690 | 0.5017 |
| verac | 0.106223 | 0.106449 | 0.9979 | 0.047864 | 2.2193 |
| ri_acsf | 0.093206 | 0.127786 | 0.7294 | 0.084970 | 1.0969 |
| ri_cr | 0.201477 | 0.126690 | 1.5903 | 0.143856 | 1.4005 |
| ri_tvf | 0.144593 | 0.127786 | 1.1315 | 0.200986 | 0.7194 |
| ribspc | 0.078890 | 0.149084 | 0.5292 | 0.026852 | 2.9380 |
| asomut | 0.136145 | 0.168920 | 0.8060 | 0.087100 | 1.5631 |
| micemp | 0.135159 | 0.168920 | 0.8001 | 0.092545 | 1.4605 |
| ri_psp | 0.359484 | 0.191670 | 1.8755 | 1.662599 | 0.2162 |
| ri_transpa | 0.481275 | 0.232265 | 2.0721 | 1.602220 | 0.3004 |
| ri_iesinap | 0.231600 | 0.253380 | 0.9140 | 0.311446 | 0.7436 |
| ri_msrl | 0.503968 | 0.255572 | 1.9719 | 0.640304 | 0.7871 |
| ri_iepsp | 0.428729 | 0.277371 | 1.5457 | 0.541524 | 0.7917 |
| ri_ai | 0.316697 | 0.319465 | 0.9913 | 0.282838 | 1.1197 |
| ri_pspapt | 0.284352 | 0.337840 | 0.8417 | 0.231131 | 1.2303 |
| ri_tsa | 0.760313 | 0.361927 | 2.1007 | 1.184836 | 0.6417 |
| ri_tar | 0.269103 | 0.383358 | 0.7020 | 0.217233 | 1.2388 |
| ri_laft | 0.711444 | 0.548990 | 1.2959 | 1.369816 | 0.5194 |
| ri_dsf | 0.805930 | 0.591220 | 1.3632 | 1.292377 | 0.6236 |
| ri_nge | 0.284692 | 0.638931 | 0.4456 | 0.069886 | 4.0737 |
| ri_ot | 0.409084 | 0.681526 | 0.6002 | 0.975397 | 0.4194 |
| consyr | 0.560574 | 0.723855 | 0.7744 | 0.415628 | 1.3487 |
| ri_secoexpo | 0.907826 | 0.745419 | 1.2179 | 1.845976 | 0.4918 |
| seggar | 0.924249 | 0.766435 | 1.2059 | 0.857318 | 1.0781 |
| ri_sef | 0.736113 | 0.809312 | 0.9096 | 1.206024 | 0.6104 |
| cedin | 1.249616 | 1.405130 | 0.8893 | 1.112074 | 1.1237 |
| ri_ii_31_12_19 | 1.398360 | 1.938566 | 0.7213 | 2.474732 | 0.5651 |

### 6. El costo: totales

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

### 7. La duración

| cifra | valor |
|---|---|
| lanzamiento (inicio_lanzador a fin_lanzador, min) | [146.6] |
| suma de los TOs (to_inicio a to_fin, min) | 146.7 |
| tramo 1 proyectado por unidades y por caracteres (min) | 148.6 y 183.5 |
| la tanda proyectada por unidades y por caracteres (min) | 1223.8 y 995.5 |

### 8. La foto del repo: antes, después y lo que cambia, por carpeta

| cifra | valor |
|---|---|
| antes (inicio, fin, entradas, sin abrir, enlaces) | ['2026-10-19 00:08:03', '2026-10-19 00:08:15', 53296, 40, 342] |
| después (inicio, fin, entradas, sin abrir, enlaces) | ['2026-10-19 02:36:23', '2026-10-19 02:36:35', 53882, 42, 342] |
| nuevos | {'data/experiment/reextraccion_v2/corpus_tanda_final/': 579, 'data/experiment/tanda_final/t2/': 7} |
| borrados | {} |
| cambiados | {'data/experiment/reextraccion_v2/e1_extractor/cache/': 1, 'data/experiment/reextraccion_v2/e3_verificador/cache/': 2, 'logs/cache_usage.jsonl': 1} |
