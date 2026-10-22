# FRENO T5 — tanda final de B6.1: el reporte de cierre y el sello del tramo 1 como respaldo (USD 0, sin API, sin commit)

Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §5 y §7, con sus notas al pie (`27bfaeb5` y `86541475`), y la enmienda 9 al protocolo entre tandas (`756a0394`), §1, punto 1; para los hallazgos, el protocolo entre tandas (§2, `:71-100`) y el pre-registro de la tanda 1 (§5.6); las decisiones de la autora, en el registro de decisiones, §89. HEAD `fe80d354`. El tercer tramo de T4 se lee desde el árbol, con los sha256 de su FRENO.

**Resultado:**
- **El reporte** está en `t5/reporte_tanda_final.md` (sha256 `6582bd52a16b03e1d0b7b5f965ff12f0bdfc22bf9790ff570dffae7f02e78926`).
- **El costo real:** USD 97,598343 (E1 48,246829, E3 49,351514), 0,9317 del estimado del §3 con las líneas de alcance (104,749805). El tramo 1: 12,856189 contra 12,690115 (1,0131); el tramo 2: 84,742154 contra 91,850250 (0,9226).
- **Los ids de modelo:** los esperados, en E1, en los reintentos de E1 de la fase de E3 y en E3: sí.
- **Los hallazgos:** 12; propuestas de entrada del backlog: 5 (`t5/propuestas_backlog_t5.jsonl`). Las 16 de las aceptadas no ítems llevan «causa: en la clasificación de la autora».
- **El freno de T4** (aceptadas no ítems, atención sobre las 60: tasa 0,3733, umbral 0,2437) va en el reporte con la línea del §89.
- **El sello del tramo 1** (sección 6): su costo, su columna del tablero (contada con el código de T3 sobre una copia: T3 no la había contado), el sha256 de sus 30 carpetas (el del cierre del tramo 1 no está en los FRENOs de T1 ni de T2) y el registro de sus dos grafos en `grafos.py`, con su vista y su control: OK. No cargué nada en Neo4j.
- **El `NO_ABRIR_`:** `t5/NO_ABRIR_conteos_t5.json`, sha256 `d2e9f96ee92f804b8841c93cb4e19993dd001ee4c97e3792fec60b9460801be2`, sin abrir.
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0

La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_T5_salida.txt`, de `paso0_t5.sh`, con `paso0_sha_tramo3_t5.py`, `foto_repo_sin_clasificacion_t5.py` y `paso0_foto_contra_commits_t5.py`, en el paquete):

```
== pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
== git log -4 --format='%h %s'
fe80d354 Registro de decisiones: la clasificacion del freno de la cuarta etapa, el sello del tramo 1 como respaldo, el orden de las corridas de la evaluacion final y la enmienda del juez v2 para firmar
ca5d192f Banco: cada sesion del agente con un entorno desde un conjunto cerrado de variables permitidas, su propia carpeta de configuracion y el cwd fuera del repo, con el lanzador registrado
368d50a3 Registro de decisiones: la direccion de Neo4j en el entorno de los agentes, la quinta etapa del entorno revisada, el juez v2 sobre otro modelo con su prueba sobre T, la muestra de T y el freno de la cuarta etapa de la tanda final
a4911b53 Tanda final: la cuarta etapa, la lectura de la autora de la ampliacion de las aceptadas no items, sellada y controlada
== git diff --name-only a4911b53 HEAD
data/experiment/banco_mcp/a2_1/lanzar_agente_a2_1.py
data/experiment/banco_mcp/agentes/contrato_metadata.md
data/experiment/banco_mcp/agentes/lanzar_agente.py
data/experiment/banco_mcp/agentes/selftest_entorno_limpio.py
docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md
== git status --porcelain --untracked-files=no (entre las dos rayas)
--
--
== los ocho archivos y los cuatro scripts del tercer tramo de T4 contra la sección 11 de su FRENO
igual data/experiment/tanda_final/t4/consola_tablas_t4t3_tf.txt
igual data/experiment/tanda_final/t4/tablas_t4_tramo3.md
igual data/experiment/tanda_final/t4/tasas/consola_tasas_t4t3_tf.txt
igual data/experiment/tanda_final/t4/tasas/consola_verif_tasas_independiente_t4t3_tf.txt
igual data/experiment/tanda_final/t4/tasas/distribuciones_bajo_H0_t4_tramo3.json
igual data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json
igual data/experiment/tanda_final/t4/tasas/umbrales_t4_por_celdas_mesa_al_importar_t4t3_tf.json
igual data/experiment/tanda_final/t4/tasas/verif_tasas_independiente_t4t3_tf.json
igual t4/scripts/freno_t4t3_foto_tf.py
igual t4/scripts/tablas_t4t3_tf.py
igual t4/scripts/tasas_t4t3_tf.py
igual t4/scripts/verif_tasas_independiente_t4t3_tf.py
archivos 8, scripts 4, todos iguales: True
rc=0
== data/experiment/tanda_final/t5/
no existe
== pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"
rc=1
== la foto final del tercer tramo (t4t2_fotos/foto_repo_final_T4t3.json)
04bfcfc53776ef2bdb1702e4a8d90cddd12cb6495cacbe5604da4de144c101a6
== la foto nueva, sin t4/clasificacion_freno/ (t4t2_fotos/foto_repo_antes_T5.json), contra la final del tercer tramo
2026-10-22 13:40:51 2026-10-22 13:41:05 58145 entradas
{
 "foto_anterior": {
  "sha256": "04bfcfc53776ef2bdb1702e4a8d90cddd12cb6495cacbe5604da4de144c101a6"
 },
 "foto_nueva": {
  "sha256": "1375f8dd2bd9a0fef72e8ca6250ae88fd659e14269faff0dfcf0d44397694ee3",
  "n": 58145,
  "inicio": "2026-10-22 13:40:51",
  "fin": "2026-10-22 13:41:05",
  "sin_abrir": 45,
  "enlaces": 342
 },
 "excluida_de_las_dos": "data/experiment/tanda_final/t4/clasificacion_freno/",
 "en_la_foto_nueva_bajo_la_excluida": 0,
 "commits": "a4911b53..HEAD",
 "rutas_en_los_commits": {
  "docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md": "M"
 },
 "nuevos": [
 ],
 "borrados": [],
 "cambiados": [
  "docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md"
 ],
 "DS_Store": [],
 "fuera_de_los_commits": [],
 "rutas_de_los_commits_distintas_de_HEAD": [],
 "ok": true
}
rc=0
== .pyc: líneas y diff contra los del final del tercer tramo
   11236
iguales
== hora
2026-10-22 13:41:05
```

La impresión de la comparación de arriba sale filtrada: el filtro de `paso0_t5.sh` sacó los renglones de las rutas (sección 13, punto 1). Las listas completas, de `foto_contra_commits_T5.json`:
- **las rutas de los commits** `a4911b53..HEAD`: `data/experiment/banco_mcp/a2_1/lanzar_agente_a2_1.py` (M); `data/experiment/banco_mcp/agentes/contrato_metadata.md` (M); `data/experiment/banco_mcp/agentes/lanzar_agente.py` (M); `data/experiment/banco_mcp/agentes/selftest_entorno_limpio.py` (A); `docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md` (M);
- **nuevas:** `data/experiment/banco_mcp/agentes/selftest_entorno_limpio.py`; **cambiadas:** `data/experiment/banco_mcp/a2_1/lanzar_agente_a2_1.py`, `data/experiment/banco_mcp/agentes/contrato_metadata.md`, `data/experiment/banco_mcp/agentes/lanzar_agente.py`, `docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md`; **borradas:** ninguna;
- **fuera de los commits:** 0; **`.DS_Store`:** 0; **distintas de HEAD:** 0. Las rutas de los commits son, byte a byte, las de `git show HEAD:`.
- **El 157 v2 y el 158:** debajo del 159 están `ca5d192f` (el commit del banco, con los cuatro archivos de `banco_mcp/`: el 157 v2) y `368d50a3` (el registro de decisiones: el 158). El 160 no entró.
- **La foto nueva no entra en `t4/clasificacion_freno/`:** `foto_repo_sin_clasificacion_t5.py` importa la foto de T1 sin cambiarla (su sha256 se controla) y saca esa carpeta de la recorrida antes de bajar a ella. Está guardada en `t4t2_fotos/`.

## 2. El costo, por etapa, por tramo y por TO, con la desviación (§7)

Las tablas 3, 4 y 5 del reporte, tal cual (de `t5/salidas/cifras_t5.json`, `costo`):

#### Tabla 3. Por etapa y por tramo, en USD (`costo.por_tramo` y `costo.total`)

| | E1 real | E3 real | total real | estimado del §3 | razón | estimado repartido (manifiesto) | razón |
|---|---:|---:|---:|---:|---:|---:|---:|
| tramo 1 | 6,647885 | 6,208304 | 12,856189 | 12,690115 | 1,0131 | 19,310012 | 0,6658 |
| tramo 2 | 41,598944 | 43,143210 | 84,742154 | 91,850250 | 0,9226 | 85,439791 | 0,9918 |
| tanda final | 48,246829 | 49,351514 | 97,598343 | 104,749805 | 0,9317 | 104,749803 | 0,9317 |

#### Tabla 4. La desviación por etapa, en USD (real − estimado)

| | E1 contra el §3 | E3 contra el §3 | total contra el §3 | E1 contra el repartido | E3 contra el repartido | total contra el repartido |
|---|---:|---:|---:|---:|---:|---:|
| tramo 1 | 0,556750 | -0,390676 | 0,166074 | -2,684073 | -3,769750 | -6,453823 |
| tramo 2 | -2,488306 | -4,619790 | -7,108096 | 0,512686 | -1,210323 | -0,697637 |
| tanda final | -2,140996 | -5,010466 | -7,151462 | -2,171387 | -4,980073 | -7,151460 |

- **El estimado del §3:** por tramo, 12,690115 y 91,850250: U × 0,021115, sin las líneas de alcance, como las cifras del §3; en total, con las líneas (A3.costo_lineas_usd), 104,749805. Por etapa, con las tarifas del manifiesto (e1 0,010135 más las líneas; e3 0,010980).
- **El estimado repartido** es el del manifiesto, por TO (nota `27bfaeb5`): el que usó la proyección del runner. Va al lado.
- **El presupuesto compartido:** USD 97,598344 de un tope de 151,5835 (0,6439 del tope). La suma de las fases da 97,598343: la diferencia, -0,000001, es de redondeo. El resumen de T2 da la misma suma por TO: sí.
- **Los pasos sin API** van en 0: E0, E2 y el validador, ensamblado, T3 (ensamblados, gate, registro y lo contado), T4 (sorteos, material y lecturas), T5.
- **E3 va como una sola cifra por TO,** con los reintentos adentro (cegamiento).
- **La tanda 1 al lado** (hueco `T5.costo_real_tanda1`, `data/experiment/tanda1/t5/salidas/costo_t5.json`, clave `para_el_preregistro_tanda_final`, en `0c2befad`), tal cual: «E1: real USD 35,5293, estimado USD 33,5350, razón 1,0595; E3: real USD 35,4617, estimado USD 36,1242, razón 0,9817; total: real USD 70,9910, estimado USD 69,6592, razón 1,0191».

- **El estimado del §3:** por tramo, 12,690115 y 91,850250: U × 0,021115, sin las líneas de alcance, como las cifras del §3; en total, con las líneas (A3.costo_lineas_usd), 104,749805. Por etapa, con las tarifas del manifiesto (e1 0,010135 más las líneas; e3 0,010980).
- **El estimado repartido** es el del manifiesto, por TO (nota `27bfaeb5`): el que usó la proyección del runner. Va al lado.
- **El presupuesto compartido:** USD 97,598344 de un tope de 151,5835 (0,6439 del tope). La suma de las fases da 97,598343: la diferencia, -0,000001, es de redondeo. El resumen de T2 da la misma suma por TO: sí.
- **Los pasos sin API** van en 0: E0, E2 y el validador, ensamblado, T3 (ensamblados, gate, registro y lo contado), T4 (sorteos, material y lecturas), T5.
- **E3 va como una sola cifra por TO,** con los reintentos adentro (cegamiento).
- **La tanda 1 al lado** (hueco `T5.costo_real_tanda1`, `data/experiment/tanda1/t5/salidas/costo_t5.json`, clave `para_el_preregistro_tanda_final`, en `0c2befad`), tal cual: «E1: real USD 35,5293, estimado USD 33,5350, razón 1,0595; E3: real USD 35,4617, estimado USD 36,1242, razón 0,9817; total: real USD 70,9910, estimado USD 69,6592, razón 1,0191».

#### Tabla 5. Por TO, en USD (`costo.por_to`; el estimado, el del manifiesto)

| TO | tramo | E1 real | E3 real | total real | estimado | desviación | razón |
|---|---|---:|---:|---:|---:|---:|---:|
| asomut | 1 | 0,065476 | 0,070669 | 0,136145 | 0,087100 | 0,049045 | 1,5631 |
| cedin | 1 | 0,636939 | 0,612677 | 1,249616 | 1,112074 | 0,137542 | 1,1237 |
| consyr | 1 | 0,286176 | 0,274398 | 0,560574 | 0,415628 | 0,144946 | 1,3487 |
| micemp | 1 | 0,057661 | 0,077498 | 0,135159 | 0,092545 | 0,042614 | 1,4605 |
| ri_acsf | 1 | 0,049436 | 0,043770 | 0,093206 | 0,084970 | 0,008236 | 1,0969 |
| ri_ai | 1 | 0,169304 | 0,147393 | 0,316697 | 0,282838 | 0,033859 | 1,1197 |
| ri_bdp | 1 | 0,063773 | 0,052535 | 0,116308 | 0,063716 | 0,052592 | 1,8254 |
| ri_cr | 1 | 0,055560 | 0,145917 | 0,201477 | 0,143856 | 0,057621 | 1,4005 |
| ri_dsf | 1 | 0,393876 | 0,412054 | 0,805930 | 1,292377 | -0,486447 | 0,6236 |
| ri_esd | 1 | 0,053522 | 0,035627 | 0,089149 | 0,177690 | -0,088541 | 0,5017 |
| ri_ieccm | 1 | 0,026238 | 0,031398 | 0,057636 | 0,019651 | 0,037985 | 2,9330 |
| ri_iepsp | 1 | 0,226702 | 0,202027 | 0,428729 | 0,541524 | -0,112795 | 0,7917 |
| ri_iesinap | 1 | 0,127673 | 0,103927 | 0,231600 | 0,311446 | -0,079846 | 0,7436 |
| ri_ii_31_12_19 | 1 | 0,727515 | 0,670845 | 1,398360 | 2,474732 | -1,076372 | 0,5651 |
| ri_laft | 1 | 0,345365 | 0,366079 | 0,711444 | 1,369816 | -0,658372 | 0,5194 |
| ri_msrl | 1 | 0,280705 | 0,223263 | 0,503968 | 0,640304 | -0,136336 | 0,7871 |
| ri_nge | 1 | 0,146852 | 0,137840 | 0,284692 | 0,069886 | 0,214806 | 4,0737 |
| ri_ot | 1 | 0,224127 | 0,184957 | 0,409084 | 0,975397 | -0,566313 | 0,4194 |
| ri_psp | 1 | 0,175381 | 0,184103 | 0,359484 | 1,662599 | -1,303115 | 0,2162 |
| ri_pspapt | 1 | 0,130272 | 0,154080 | 0,284352 | 0,231131 | 0,053221 | 1,2303 |
| ri_rcl | 1 | 0,044966 | 0,029028 | 0,073994 | 0,071423 | 0,002571 | 1,0360 |
| ri_secoexpo | 1 | 0,469175 | 0,438651 | 0,907826 | 1,845976 | -0,938150 | 0,4918 |
| ri_sef | 1 | 0,346036 | 0,390077 | 0,736113 | 1,206024 | -0,469911 | 0,6104 |
| ri_tar | 1 | 0,144124 | 0,124979 | 0,269103 | 0,217233 | 0,051870 | 1,2388 |
| ri_transpa | 1 | 0,308535 | 0,172740 | 0,481275 | 1,602220 | -1,120945 | 0,3004 |
| ri_tsa | 1 | 0,495321 | 0,264992 | 0,760313 | 1,184836 | -0,424523 | 0,6417 |
| ri_tvf | 1 | 0,085143 | 0,059450 | 0,144593 | 0,200986 | -0,056393 | 0,7194 |
| ribspc | 1 | 0,040386 | 0,038504 | 0,078890 | 0,026852 | 0,052038 | 2,9380 |
| seggar | 1 | 0,427097 | 0,497152 | 0,924249 | 0,857318 | 0,066931 | 1,0781 |
| verac | 1 | 0,044549 | 0,061674 | 0,106223 | 0,047864 | 0,058359 | 2,2193 |
| actgar | 2 | 0,465845 | 0,580240 | 1,046085 | 0,551338 | 0,494747 | 1,8974 |
| adfsp | 2 | 1,009634 | 0,871772 | 1,881406 | 2,231107 | -0,349701 | 0,8433 |
| afiltr | 2 | 0,986726 | 0,921125 | 1,907851 | 2,977481 | -1,069630 | 0,6408 |
| apnf | 2 | 0,306159 | 0,316085 | 0,622244 | 0,755376 | -0,133132 | 0,8238 |
| autenf | 2 | 0,667893 | 0,792561 | 1,460454 | 1,413508 | 0,046946 | 1,0332 |
| cateloc | 2 | 0,318502 | 0,693195 | 1,011697 | 3,912391 | -2,900694 | 0,2586 |
| ccbcra | 2 | 0,270482 | 0,240107 | 0,510589 | 0,317440 | 0,193149 | 1,6085 |
| cescar | 2 | 0,183822 | 0,305087 | 0,488909 | 0,274780 | 0,214129 | 1,7793 |
| coltit | 2 | 0,278253 | 0,276862 | 0,555115 | 0,275636 | 0,279479 | 2,0139 |
| convca | 2 | 0,116368 | 0,109536 | 0,225904 | 0,172553 | 0,053351 | 1,3092 |
| cryl | 2 | 0,638023 | 0,661718 | 1,299741 | 1,128980 | 0,170761 | 1,1513 |
| ctacor | 2 | 0,197485 | 0,244739 | 0,442224 | 0,611651 | -0,169427 | 0,7230 |
| ctavis | 2 | 2,288129 | 2,584113 | 4,872242 | 3,682072 | 1,190170 | 1,3232 |
| depinv | 2 | 1,653077 | 1,572888 | 3,225965 | 2,202301 | 1,023664 | 1,4648 |
| disres | 2 | 0,466974 | 0,493544 | 0,960518 | 1,087988 | -0,127470 | 0,8828 |
| evacre | 2 | 0,150588 | 0,193924 | 0,344512 | 0,226630 | 0,117882 | 1,5202 |
| fabcra | 2 | 0,432891 | 0,394999 | 0,827890 | 1,106541 | -0,278651 | 0,7482 |
| fclef | 2 | 0,221151 | 0,199007 | 0,420158 | 0,287449 | 0,132709 | 1,4617 |
| fgarcp | 2 | 0,256384 | 0,203609 | 0,459993 | 0,446762 | 0,013231 | 1,0296 |
| fimipyme | 2 | 0,507990 | 0,610693 | 1,118683 | 0,745869 | 0,372814 | 1,4998 |
| finsec | 2 | 1,374430 | 1,668692 | 3,043122 | 3,848192 | -0,805070 | 0,7908 |
| garant | 2 | 0,933732 | 0,998828 | 1,932560 | 2,266457 | -0,333897 | 0,8527 |
| garopt | 2 | 0,384223 | 0,435103 | 0,819326 | 0,385680 | 0,433646 | 2,1244 |
| gescre | 2 | 0,696062 | 0,581931 | 1,277993 | 1,220405 | 0,057588 | 1,0472 |
| gracre | 2 | 0,587947 | 0,682780 | 1,270727 | 0,707995 | 0,562732 | 1,7948 |
| graloc | 2 | 0,978134 | 1,056755 | 2,034889 | 1,973563 | 0,061326 | 1,0311 |
| horari | 2 | 0,152656 | 0,117590 | 0,270246 | 0,358454 | -0,088208 | 0,7539 |
| icmecma | 2 | 0,499976 | 0,508358 | 1,008334 | 0,775422 | 0,232912 | 1,3004 |
| incuca | 2 | 0,202940 | 0,178976 | 0,381916 | 0,280576 | 0,101340 | 1,3612 |
| inspag | 2 | 0,828152 | 0,853189 | 1,681341 | 2,042988 | -0,361647 | 0,8230 |
| jafip | 2 | 0,900186 | 0,813671 | 1,713857 | 1,297800 | 0,416057 | 1,3206 |
| lavdin | 2 | 0,241873 | 0,279222 | 0,521095 | 0,353295 | 0,167800 | 1,4750 |
| opecam | 2 | 0,644880 | 0,632211 | 1,277091 | 1,155876 | 0,121215 | 1,1049 |
| ordcom | 2 | 0,453413 | 0,540613 | 0,994026 | 0,664587 | 0,329439 | 1,4957 |
| osapsa | 2 | 0,140609 | 0,135423 | 0,276032 | 0,206123 | 0,069909 | 1,3392 |
| pfmipyme | 2 | 0,384145 | 0,356228 | 0,740373 | 0,537572 | 0,202801 | 1,3773 |
| pimf | 2 | 1,417553 | 1,561038 | 2,978591 | 2,420324 | 0,558267 | 1,2307 |
| pognme | 2 | 0,163519 | 0,165338 | 0,328857 | 0,232251 | 0,096606 | 1,4160 |
| prevmi | 2 | 0,539539 | 0,730880 | 1,270419 | 0,965583 | 0,304836 | 1,3157 |
| pscpp | 2 | 0,213715 | 0,185973 | 0,399688 | 0,339045 | 0,060643 | 1,1789 |
| raapal | 2 | 0,518754 | 0,622185 | 1,140939 | 1,655442 | -0,514503 | 0,6892 |
| ratio | 2 | 1,485850 | 1,322435 | 2,808285 | 4,258373 | -1,450088 | 0,6595 |
| ratiofn | 2 | 1,144626 | 1,485535 | 2,630161 | 1,546869 | 1,083292 | 1,7003 |
| regpri | 2 | 0,179291 | 0,211014 | 0,390305 | 0,280993 | 0,109312 | 1,3890 |
| relact | 2 | 0,303781 | 0,295256 | 0,599037 | 0,354327 | 0,244710 | 1,6906 |
| repefe | 2 | 0,689578 | 0,729552 | 1,419130 | 1,308163 | 0,110967 | 1,0848 |
| reqcac | 2 | 0,204188 | 0,108961 | 0,313149 | 0,435784 | -0,122635 | 0,7186 |
| retype | 2 | 0,288941 | 0,263019 | 0,551960 | 0,322512 | 0,229448 | 1,7114 |
| ri2_ci | 2 | 0,636166 | 0,590189 | 1,226355 | 1,924359 | -0,698004 | 0,6373 |
| rmgcti | 2 | 1,547298 | 1,055621 | 2,602919 | 3,898339 | -1,295420 | 0,6677 |
| rmrtsd | 2 | 0,404829 | 0,393772 | 0,798601 | 1,214696 | -0,416095 | 0,6574 |
| rrci | 2 | 0,707737 | 0,720239 | 1,427976 | 1,766957 | -0,338981 | 0,8082 |
| secfin | 2 | 0,169664 | 0,209566 | 0,379230 | 0,300161 | 0,079069 | 1,2634 |
| seguef | 2 | 0,897786 | 0,998910 | 1,896696 | 1,722056 | 0,174640 | 1,1014 |
| servco | 2 | 0,323275 | 0,442634 | 0,765909 | 0,511598 | 0,254311 | 1,4971 |
| snp_atm | 2 | 0,133250 | 0,109074 | 0,242324 | 0,171784 | 0,070540 | 1,4106 |
| snp_cec | 2 | 1,166043 | 1,137668 | 2,303711 | 2,449987 | -0,146276 | 0,9403 |
| snp_dd | 2 | 1,297895 | 1,101092 | 2,398987 | 3,853900 | -1,454913 | 0,6225 |
| snp_debin | 2 | 0,639856 | 0,549768 | 1,189624 | 0,868010 | 0,321614 | 1,3705 |
| snp_mep | 2 | 0,810357 | 0,646331 | 1,456688 | 2,215958 | -0,759270 | 0,6574 |
| snp_psp | 2 | 0,819684 | 0,882260 | 1,701944 | 1,445213 | 0,256731 | 1,1776 |
| snp_spd | 2 | 1,105102 | 1,178017 | 2,283119 | 1,711342 | 0,571777 | 1,3341 |
| snp_tr_nc | 2 | 1,191036 | 1,143172 | 2,334208 | 1,607578 | 0,726630 | 1,4520 |
| socgar | 2 | 0,124081 | 0,115155 | 0,239236 | 0,167217 | 0,072019 | 1,4307 |
| supcon | 2 | 0,501555 | 0,707654 | 1,209209 | 0,958118 | 0,251091 | 1,2621 |
| tasint | 2 | 0,585999 | 0,682552 | 1,268551 | 0,942046 | 0,326505 | 1,3466 |
| traval | 2 | 0,334410 | 0,452732 | 0,787142 | 0,767386 | 0,019756 | 1,0257 |
| venliq | 2 | 0,233852 | 0,240244 | 0,474096 | 0,340582 | 0,133514 | 1,3920 |

Mis aclaraciones:
- **El costo de cada fase** es su `gasto_usd` en `estado_corpus.json`; el resumen de E3 de cada fase trae el desglose por estado, que no se lee. E3 va como una sola cifra por TO, con los reintentos adentro.
- **El estimado del §3 por tramo** no lleva las líneas de alcance, como las cifras del §3 (12,6901 y 91,8502); el total, sí. El repartido es el que usó la proyección del runner, y va al lado.
- **La tanda 1** es solo la cadena del hueco `T5.costo_real_tanda1`, leída con `git show 0c2befad:` y su clave: es lo único de la tanda 1 que leí.

## 3. Los ids de modelo

| etapa | ids | llamadas | lo esperado | igual |
|---|---|---|---|---|
| E1 | claude-haiku-4-5-20251001 | claude-haiku-4-5-20251001: 4.997 | claude-haiku-4-5-20251001 | sí |
| reintentos de E1 de la fase de E3 | claude-haiku-4-5-20251001 | en el `NO_ABRIR_` | claude-haiku-4-5-20251001 | sí |
| E3 | claude-sonnet-5 | en el `NO_ABRIR_` | claude-sonnet-5 | sí |

Lo esperado sale del pre-registro de la tanda final, §2; no nombra ids de modelo; los esperados salen del pre-registro de la tanda final, §2. El freno por modelo de T2: OK, con claude-haiku-4-5-20251001 en E1 y claude-sonnet-5 en E3 (t2/FRENO_T2.md, resultado).
Las llamadas de E1 incluyen sus reintentos y las partes; las de E3 cuentan los reintentos de E3 y van solo al `NO_ABRIR_`.

## 4. Los hallazgos y las propuestas del backlog

Qué es un hallazgo: una fila del tablero que no cumple su meta, una incorrecta de las lecturas de T4, una vigilancia fuera de su línea de base, una regresión declarada de T3 y la cola con la regla del 25 % disparada (protocolo entre tandas, §2; pre-registro de la tanda 1, §5.6). La causa de las incorrectas sale de la lectura de la autora; la de las aceptadas no ítems, de su clasificación.

| id | qué | cifra | eje A | eje B | `capa_pipeline` | causa | backlog |
|---|---|---|---|---|---|---|---|
| H-T5-01 | fila del tablero que no cumple su meta (61): Unidades cortadas o mudas | 1 de 4.951: ri_transpa::Sbloque1::chapeau_seccion; la misma es el error definitivo de T2 | F08c (reintento por salida de E1 mal formada): «E1 y E3 de las afectadas» | se difiere: el runner es código sellado (pre-registro, §8) | corrida | la de BKL-0050: el reintento por forma de E1 corta en 8.192 sin escalar | ya está: BKL-0050 |
| H-T5-02 | fila del tablero que no cumple su meta (67): Cuantías sin campo estructurado | 14 sin campo de 1297 con cuantía (Condicion 2, Obligacion 12) | F15b (umbrales del ensamblado): «solo código sobre lo guardado» | puede corregirse con código antes del sello del grafo evaluado (re-aplicación única); sin una corrección lista, se difiere | ensamblado | lo contado no la da: son nodos con cuantía en la descripción y sin `umbral` ni `plazo` (la regex de la fila, c14) | propuesta (`PROP-T5-01`) |
| H-T5-03 | incorrecta de la lectura de T4: observación (12): una arista `aplica_a` al rol de alcance de otro TO | 1 de 30; arista 45358f0c7878 (código: los 12 primeros caracteres del sha256 del id) | F15d (sujetos por relación, reglas R1 a R4): «solo código sobre lo guardado» | puede corregirse con código antes del sello del grafo evaluado; sin una corrección lista, se difiere | catálogo | la de la lectura de la autora: «incorrecta (catálogo)», el destino es el rol de alcance de otro TO, que la resolución tomó de la sugerencia del modelo (criterio O12-sujeto-de-otro-TO) | propuesta (`PROP-T5-02`) |
| H-T5-04 | incorrectas de la lectura de T4: aceptadas no ítems (sobre las 60), con el freno: las unidades con error de no ítems | 16 de 60; tasa ponderada 0,3733; freno por la atención sobre las 60: sí | según la clasificación de la autora | según la clasificación de la autora (registro de decisiones, §89) | — | en la clasificación de la autora (t4/clasificacion_freno/) | la decide la clasificación |
| H-T5-05 | incorrectas de la lectura de T4: aceptadas ítems: las unidades con error de ítems | 6 de 30; por la regla de la propuesta que la lectura confirma: U-no-sostenida 4, veredicto cambiado por la autora (causa en su nota) 2 | según la capa de cada una | según la capa de cada una | — | la de cada unidad, de la lectura de la autora (errores_de_las_lecturas.aceptadas_items); la planilla de T4 no tiene la capa | propuesta (`PROP-T5-03`) |
| H-T5-06 | incorrectas de la lectura de T4: la cola, con la regla del 25 % disparada: las unidades con error de la cola | 12 de 30; tasa ponderada 0,3706, Wilson [0,2057; 0,5723]; la regla del 25 % se dispara: sí; por la regla de la propuesta que la lectura confirma: U-no-sostenida 2, U-tipo 3, veredicto cambiado por la autora (causa en su nota) 7 | según la capa de cada una | la cola no entra al grafo sin cola; la regla del 25 % es cifra y vigilancia, no freno | — | la de cada unidad, de la lectura de la autora (errores_de_las_lecturas.cola); la planilla de T4 no tiene la capa | propuesta (`PROP-T5-04`) |
| H-T5-07 | vigilancia fuera de su línea de base (vigilancia:1): Condicion que lleva un deber explícito | 7 de 30, Wilson [0,1179; 0,4093]; tanda 1 3 de 30 | F06 (prefijo de E1): «todo» | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (protocolo, §2, eje B) | E1-prompt | la de la lectura: la Condicion recoge un deber que el texto formula como tal (V1-deber); la tipa E1 | propuesta (`PROP-T5-05`) |
| H-T5-08.1 | regresión declarada de T3: RT-C5-3 | declarada en el gate de T3 (acumulado de las tres) | nada: residuo declarado | residuo declarado (laudo) | — | la del laudo | no |
| H-T5-08.2 | regresión declarada de T3: RT-C6-1 | declarada en el gate de T3 (acumulado de las tres) | nada: residuo declarado | residuo declarado (laudo) | — | la del laudo | no |
| H-T5-08.3 | regresión declarada de T3: RT-C6-2 | declarada en el gate de T3 (acumulado de las tres) | nada: residuo declarado | residuo declarado (laudo) | — | la del laudo | no |
| H-T5-08.4 | regresión declarada de T3: E4-a1 | declarada en el gate de T3 (acumulado de las tres) | la de BKL-0048 | se difiere (BKL-0048) | E1-prompt | la de BKL-0048 | ya está: BKL-0048 |
| H-T5-08.5 | regresión declarada de T3: E4-a4 | declarada en el gate de T3 (acumulado de las tres) | la de BKL-0048 | se difiere (BKL-0048) | E1-prompt | la de BKL-0048 | ya está: BKL-0048 |

**Las vigilancias leídas contra su línea de base** (propuesta de la ejecutora: una vigilancia leída está fuera de su línea de base si la de la tanda 1 cae fuera del Wilson de la tanda final; es un hallazgo si además la cifra empeora. Las contadas sin leer, (4), (5), (8) y (9), no tienen intervalo: van con su cifra y la de la tanda 1 al lado, sin juicio):

| vigilancia | tanda final | Wilson | tanda 1 | fuera | empeora | hallazgo |
|---|---|---|---|---|---|---|
| vigilancia:1 | 7 de 30 | [0,1179; 0,4093] | 3 de 30 | sí | sí | sí |
| vigilancia:2 | 6 de 30 | [0,0951; 0,3731] | 15 de 30 | sí | no | no |
| vigilancia:3 | 5 de 30 | [0,0734; 0,3356] | 9 de 30 | no | no | no |
| vigilancia:7 | 2 de 6 | [0,0968; 0,7000] | 2 de 4 | no | no | no |

Las causas de cada unidad con error de la cola y de las aceptadas de ítems (de la lectura de la autora) están en `errores_de_las_lecturas` de `t5/salidas/cifras_t5.json`; las 16 de no ítems, con «causa: en la clasificación de la autora (`t4/clasificacion_freno/`)». Lo diferido va como propuesta de entrada del backlog en `t5/propuestas_backlog_t5.jsonl`: `PROP-T5-01`, `PROP-T5-02`, `PROP-T5-03`, `PROP-T5-04`, `PROP-T5-05`.

**Las propuestas** (`t5/propuestas_backlog_t5.jsonl`; el backlog no se tocó):

| id | `capa_pipeline` | eje A | eje B | causa |
|---|---|---|---|---|
| PROP-T5-01 | ensamblado | F15b, solo código sobre lo guardado | se difiere sin una corrección lista | 14 nodos con cuantía en la descripción y sin `umbral` ni `plazo` (fila 67 del tablero); la meta los admite solo como el residuo de diez |
| PROP-T5-02 | catálogo | F15d, solo código sobre lo guardado | se difiere sin una corrección lista | la (12): el `aplica_a` va al rol de alcance de otro TO, que la resolución del sujeto tomó de la sugerencia del modelo |
| PROP-T5-03 | — | según la capa | según la capa | 6 unidades aceptadas de ítems con error en la lectura de la autora; la causa de cada una, en errores_de_las_lecturas.aceptadas_items de t5/salidas/cifras_t5.json |
| PROP-T5-04 | — | según la capa | según la capa | 12 unidades de la cola con error en la lectura de la autora y la regla del 25 % disparada; la causa de cada una, en errores_de_las_lecturas.cola de t5/salidas/cifras_t5.json |
| PROP-T5-05 | E1-prompt | F06, todo | se difiere: fuera del grafo que evalúa B6.3 | la vigilancia (1) sube contra la línea de base de la tanda 1: Condicion que llevan un deber explícito |

Mis aclaraciones:
- **El tablero contra su meta:** el criterio de cada fila está en el reporte (sección 6) y en `tablero_contra_su_meta`. Lo escribí yo; las filas 50, 52 y 64 son las que más pueden pesar (la 50 no se decide con lo contado; en la 52 rige la parte medible de la meta; en la 64, la Comunicacion sin `tipo` es el residuo que la meta declara).
- **Las vigilancias:** el criterio de «fuera de su línea de base» también es mío (está en `vigilancias_contra_su_linea_de_base`). Con él, la (1) es hallazgo; la (2) queda fuera, pero mejora.
- **La cola y las aceptadas de ítems:** la planilla de T4 no tiene la capa. Van con la causa que da la lectura de la autora, unidad por unidad (`errores_de_las_lecturas`), y como propuestas a clasificar (PROP-T5-03 y PROP-T5-04), sin inferir la capa.
- **Los ids de nodos y aristas** van por su código (los 12 primeros caracteres del sha256 del id); las causas citan solo texto de unidades a la vista de T4. No hizo falta `t5/unidades_a_la_vista_T5.json`.

## 5. El reporte

`t5/reporte_tanda_final.md` (sha256 `6582bd52a16b03e1d0b7b5f965ff12f0bdfc22bf9790ff570dffae7f02e78926`), de `t5/scripts/reporte_t5_tf.py`: los volúmenes, el costo, los ids de modelo, las incidencias, las tasas de T4 con el freno, la columna del tablero (completa, como propuesta, en `t5/columna_tanda_final_tablero_PROPUESTA.md`, sha256 `776f80cacfc83631148550ced74038e6567947196c8eb1f560cfdb57c481fd56`), los hallazgos y lo que sigue.

## 6. El sello del tramo 1 como respaldo (enmienda 9, §1, punto 1)

- **Su costo** (`cifras_t5.json`, `sello_tramo1.costo`): USD 12,856189 (E1 6,647885, E3 6,208304), contra 12,690115 del §3 (1,0131) y 19,310012 del repartido (0,6658).
- **Su columna del tablero:** `t5/columna_tramo1_tablero_PROPUESTA.md` (sha256 `b985f9ae203b4da46bf23492260ceb9b325e4e2ffefe573acb7748e8ef88f9f7`), con el tramo 1 y su acumulado, completos y sin cola. **Lo que contó T3 no la traía** (`contado_sin_leer_tf.json` cuenta la tanda y el acumulado de las tres): la conté con el mismo código de T3 (`t5/scripts/contado_tramo1_t5.py`, copiado y adaptado) sobre una copia del repo. Para el acumulado de 60 rearmé en la copia su entrada, que T3 armó solo en la suya (`entrada_acumulado_60_t5.py`): 1.073 archivos y la misma lista que T3 (sí). El control contra el re-sellado de la tanda 0: 11 de 11. Saqué el control contra la línea de base de la tanda 1 (sus cifras están vedadas) y mandé la cola por estado al `NO_ABRIR_`.
- **Sus carpetas de salida** (`t5/salidas/carpetas_tramo1_t5.json`, de `carpetas_tramo1_t5.py`): **el sha256 tomado al cerrar el tramo 1 no está** en los FRENOs de T1 ni de T2, ni en el control entre tramos. Doy el de hoy, por TO, y el de las 30 juntas, `c78409f9696c6b99a8c8b0eb1cd4e4691403f0e734b2d6f33226eaff6e897b9a`. Al lado, un control indirecto: la entrada del acumulado de 60 que armó T3 el 20/10, después de cerrar el tramo 2, copia esas 30 carpetas, y rearmada hoy da la misma lista (arriba).

| TO | sha256 de la carpeta (hoy) |
|---|---|
| asomut | `8e98038e5d32689446f16edef5b5c166fe6d7c72cd2739d19a4c1b2fd7e7473e` |
| cedin | `7238d0b38ad1662d9af35efa54916a05a66b4056c80ef8f59bc8e70b8439275b` |
| consyr | `5b3f612f05df3b5cf43a551a5db2873a6a80b3f5b5c038a6b3b1309acc8a245a` |
| micemp | `52defb15aa6cf1068bf409e3410938e59016bf64c0a1b41df0f85260c0abd4c6` |
| ri_acsf | `0592acaf26eb5e4e2e8581b6cb6793064d5900865be4dd9988e0b159b625dbbb` |
| ri_ai | `510c7b3e86dc4f8eaa052c9e85717c3fc292ccdda1a2fb1f8d1cf6126fadb8ed` |
| ri_bdp | `abde152bd9d4b46d8cfa86ce66c70be3c349402b287163cd7c9dd6db62b92502` |
| ri_cr | `3a167c334127e9ca8fd87312e6afc7420da6e20cf13dfc5a38b925d581124741` |
| ri_dsf | `e3e68691b894801afe8d1cd75358eb9fa410b4532220a8e0bbe499ad6162fa09` |
| ri_esd | `fb54363d74e43c4ee3dc628e1ad86607ab42d512f48dd0c322467445bbb6d069` |
| ri_ieccm | `25bc8280a0df08bd9ed2bd99cb8a51d6a73350ab3d77720ca8867283807dedeb` |
| ri_iepsp | `3170d642622e1e28adf4b52041fe982923d2d4c7478c38d8adf738172a566110` |
| ri_iesinap | `6c4445d0bd873265ffc08c4112d32290f8ba53dee619432c45bca4a55faad41f` |
| ri_ii_31_12_19 | `c9b118b59bed0bf3d3cf7f4eed91202bb09b96e45b6e69269774d008b95766fe` |
| ri_laft | `6f20169a81c78c3bb8f24fde4e01abc03ac29fb867e607ee355305095dfa5a5a` |
| ri_msrl | `418a2e91af2d16ee145f444fdbde26bed4ff6369ff8613346bc2818c81434117` |
| ri_nge | `62e617b7663d11f80f0860a219c956802caf1c5be54dcc81ab8f6b1fcd629b09` |
| ri_ot | `5e4caea3ca99fb8abf36b8f45856ad7cfa7f5a05ba8cd22f81fd3441ee02eb48` |
| ri_psp | `0b47202edf787e9e02599a7677b03f650574b3049c34aeb15b53b61c68a08361` |
| ri_pspapt | `3946df8efed4fa435b9514018738d568e586069f95629ab2c3bc209d83774fdb` |
| ri_rcl | `9c2cfe22af3878d72d107b03cfc637d03b88adf52e4c7c97d0b83bed76e40aa3` |
| ri_secoexpo | `1e53823d002eceb18bf94f0bcbbc3ef624c82b7e25d5ed6c526844341948fe7b` |
| ri_sef | `dcb3a1e1dc646e45af21aef4b7bf30d0d4c1ae1b7688599b507d356edf2dd74a` |
| ri_tar | `c4d5855cfd0050e401e705c343319e3b686e1fe10d5e4156e54d0bd87d0d592c` |
| ri_transpa | `0555d9d0a7dbe287ec7969ed720034fb6c5eb33244fdb68f37b01062696c7733` |
| ri_tsa | `7baa6a3a093dd33e1b8e45aea118fc7108d91ec3a6d667883450d2855f16adca` |
| ri_tvf | `cf4c713bce9114a894f34ad2047ffc97066168152af382bc04d436fb430a9736` |
| ribspc | `4ce6140c89db198f95baab295e28702a194f1017f1cf864f308d6d37681b9c90` |
| seggar | `ebab5f79392468b304dbe87de58658cbc7d979bc5821aeb808f18df6377b9e54` |
| verac | `9c6f36808ae1c3feca9d982ec1d560dcd6da3e331a6c6ae2b99a44a8d0c5bc1a` |

- **El registro de sus dos grafos** (`t5/scripts/editar_grafos_t5.py`, el de T3 adaptado, corrido sobre la copia; el repo recibió después los mismos bytes):
  - `data/experiment/neo4j/grafos.py`: dos entradas al final de `GRAFOS`, con la forma de `KG_TandaFinal_r2b`, `commit_sellado` «PENDIENTE» y los sha256 y conteos de la tabla E1 de T3. Nada más cambia: las 17 entradas selladas, iguales (sí); solo dos nuevas (sí). sha256 de `grafos.py`: antes `89aaaaca7f7e550c0837cfa5f3d2189bebf8d9a724ba4f2a851ce7bee5361c22`; después `b5be8fd1abae0d870f963ea92fda21a15c3f7be4f01bf7687704e194f83be6a7`, igual en la copia controlada. No está entre las 78 rutas del código de la cadena.
  - la vista: `t5/registro_vista_r2b_tramo1.py` (sha256 `4d61bb1fb87c34e7f88fe94e3a4009cc8daec574a8daabefbd81ec931578743b`), con el patrón de `t3/registro_vista_r2b_tanda_final.py`, que no edité; las entradas la nombran en `requiere_registro_dir` y `requiere_registro_modulo`.
  - **el control** (`t5/scripts/control_registro_tramo1_t5.py`, el control en seco de T3 adaptado, sobre la copia; `t5/salidas/control_registro_tramo1_t5.json`): KG_TandaFinal_Tramo1_r2b: sha256 sí, vista 2.372 / 4.066 contra el registro 2.372 / 4.066 (sí); KG_TandaFinal_Tramo1_r2b_sincola: sha256 sí, vista 2.207 / 3.822 contra el registro 2.207 / 3.822 (sí); el desglose de «punto sin nodos», igual a lo declarado (sí). Resultado: OK.
  - **No cargué nada en Neo4j.** El control sigue el camino de imports del cargador hasta antes de tocar Neo4j.
- **Lo que entra en el commit del sello del tramo 1** (lo arma la mesa): las salidas del sello del tramo 1 y las dos entradas de `grafos.py`:
  - `data/experiment/neo4j/grafos.py` (las dos entradas) y `data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py`;
  - `t5/columna_tramo1_tablero_PROPUESTA.md`;
  - `t5/salidas/`: `contado_tramo1_t5.json`, `consola_contado_tramo1_t5.txt`, `entrada_acumulado_60_t5.json`, `carpetas_tramo1_t5.json`, `control_registro_tramo1_t5.json`, `consola_control_registro_tramo1_t5.txt`, `consola_editar_grafos_t5.txt` y `escritura_registro_tramo1_t5.json`;
  - `t5/scripts/`: `entrada_acumulado_60_t5.py`, `contado_tramo1_t5.py`, `carpetas_tramo1_t5.py`, `editar_grafos_t5.py` y `control_registro_tramo1_t5.py`;
  - compartidos con el resto de T5 (lo decide la mesa): `t5/salidas/cifras_t5.json` (el costo por tramo, `sello_tramo1`), `columnas_tablero_t5.py` (arma las dos columnas) y `t5/NO_ABRIR_conteos_t5.json` (junta el `NO_ABRIR_` del tramo 1 con el de los ids).
  - El `commit_sellado` de las dos entradas se completa en el commit siguiente, como en T3.

## 7. El cegamiento

- **Ninguna cifra usa el desglose por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos aparte.** Lo que los usa va a `t5/NO_ABRIR_conteos_t5.json` (sha256 `d2e9f96ee92f804b8841c93cb4e19993dd001ee4c97e3792fec60b9460801be2`), que junta, sin abrirlas, la cola por estado, el crudo del reintento y las `properties_no_definidas` de los grafos del tramo 1, y las llamadas por id de E3 y de los reintentos de E1 de su fase.
- **De la tanda 1** leí solo la cadena del hueco `T5.costo_real_tanda1`. El acumulado de 60 contiene la tanda 1, como en T3: su entrada copia sus carpetas de salida y lo contado lee el acumulado, sin abrir muestras, material, planillas ni cifras de la tanda 1.
- **El contenido de extracciones** que muestro es solo de unidades a la vista de T4 (las justificaciones de la lectura); los nodos y aristas van por su código.
- No abrí ningún `NO_ABRIR_` ni la carpeta `t4/clasificacion_freno/` (la copia y las fotos la excluyen), ni ningún `.env`, ni las carpetas vedadas.

## 8. Para la autora y la mesa

1. **La copia del repo** lleva, además del `rsync` de la cláusula, `--exclude=/data/experiment/tanda_final/t4/clasificacion_freno`: copiarla habría sido leerla. Lo declaro.
2. **El sha256 de las carpetas del tramo 1 al cerrarlo** no está; doy el de hoy y el control indirecto de la entrada del acumulado.
3. **Los criterios del tablero y de las vigilancias** son míos (sección 4): los decide la mesa.
4. **La capa de los errores de la cola y de ítems** no la da la lectura: van como propuestas a clasificar.
5. **El commit del sello del tramo 1:** la lista está en la sección 6; tres archivos son compartidos con el resto de T5.

## 9. La copia del repo

- `rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/tanda_final/t4/clasificacion_freno <repo>/ <copia>/`. El control antes de correr nada: 0 nombres vedados (`.env`, `.env.*`, `*.env`, `NO_ABRIR_*`) y 0 enlaces; `t4/clasificacion_freno/` en la copia: no. El log del `rsync` tiene 336 líneas, todas «skipping non-regular file». Ningún `git clone`. El control y el log van en el paquete.

## 10. Las dos corridas del script de cifras

`cifras_t5_tf.py` corrió a `t5/salidas/` y a `t5/salidas/segunda_corrida/`: los dos `cifras_t5.json` dan el mismo sha256, `17cb13d912e56c08c379e7e07e4a1ce4fa14f10620d3011b1ee1477a580553bb` (iguales: sí).

## 11. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t5_foto.py` desde la foto del paso 0 (`foto_repo_antes_T5.json`) y la de después, las dos sin `t4/clasificacion_freno/`. Las dos quedan en `t4t2_fotos/`, en la carpeta permanente de esta sesión (`fuera_del_repo/scratchpads/<sesión>/scratchpad/`), fuera del repo y del paquete porque nombran todas las rutas del repo.

- **La foto** (`t1/foto_repo_tanda_final_t1.py`). La del paso 0: 13:40:51 a 13:41:05 del 2026-10-22, 58.145 entradas, sha256 `1375f8dd2bd9a0fef72e8ca6250ae88fd659e14269faff0dfcf0d44397694ee3`. Después: 14:05:57 a 14:06:11 del 2026-10-22, 58.179 entradas, 46 sin abrir y 342 enlaces, sha256 `f042c616aac69e97fe5f83960ffa0e6602cbc379a33ae1419d0eb857430bba6e`.
  - **34 nuevos:** 6 en `tanda_final/t5/, lo demás`; 16 en `tanda_final/t5/salidas/`; 12 en `tanda_final/t5/scripts/`.
  - **0 borrados:** ninguno.
  - **3 cambiados:** 2, .DS_Store (ruido de Finder); 1, neo4j/grafos.py (las dos entradas del tramo 1).
  - **Fuera de lo admitido:** 0.
  - **Los `.DS_Store` que aparecieron o cambiaron durante T5** (ruido de Finder, fuera de lo que cuenta; su tamaño y su sha256 en la foto de después, que no guarda la hora de lo que abre): `data/experiment/tanda_final/.DS_Store`, 6148 bytes, sha256 `3b369a845a92…`; `data/experiment/tanda_final/t4/.DS_Store`, 10244 bytes, sha256 `602418003e91…`.
  - **Los `NO_ABRIR_` en `t5/`:** 1 (sin abrir; tamaño en bytes y hora de la foto de después): `data/experiment/tanda_final/t5/NO_ABRIR_conteos_t5.json`, 8036 bytes.
  - **`unidades_a_la_vista_T4.json`** (`t3/muestras/`): T5 no la toca; sha256 `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` en el paso 0 y `4b9605f2d76cee42b13597e35b0eb7652e9e2723b952d91e0e09da1f63745633` después; iguales: True.
  - **`neo4j/grafos.py`:** sha256 `89aaaaca7f7e550c0837cfa5f3d2189bebf8d9a724ba4f2a851ce7bee5361c22` en el paso 0 y `b5be8fd1abae0d870f963ea92fda21a15c3f7be4f01bf7687704e194f83be6a7` después.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos de este tramo, de la foto de después:**

| archivo | sha256 |
|---|---|
| `data/experiment/tanda_final/t5/columna_tanda_final_tablero_PROPUESTA.md` | `776f80cacfc83631148550ced74038e6567947196c8eb1f560cfdb57c481fd56` |
| `data/experiment/tanda_final/t5/columna_tramo1_tablero_PROPUESTA.md` | `b985f9ae203b4da46bf23492260ceb9b325e4e2ffefe573acb7748e8ef88f9f7` |
| `data/experiment/tanda_final/t5/propuestas_backlog_t5.jsonl` | `373bf22be4337e3a7ee77f7c6005e5fb3837303dc2fb6656c5cfb4d32d07cda1` |
| `data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py` | `4d61bb1fb87c34e7f88fe94e3a4009cc8daec574a8daabefbd81ec931578743b` |
| `data/experiment/tanda_final/t5/reporte_tanda_final.md` | `6582bd52a16b03e1d0b7b5f965ff12f0bdfc22bf9790ff570dffae7f02e78926` |
| `data/experiment/tanda_final/t5/salidas/carpetas_tramo1_t5.json` | `b1f16c125df360c69b3ee2655d6d089ca92e5011820399c44db2c3820e03df45` |
| `data/experiment/tanda_final/t5/salidas/cifras_t5.json` | `17cb13d912e56c08c379e7e07e4a1ce4fa14f10620d3011b1ee1477a580553bb` |
| `data/experiment/tanda_final/t5/salidas/consola_cifras_t5_corrida1.txt` | `38c17182d8a2c602b9de57984351f814c4f7fe65fbe6a59fafe1b213e4ced688` |
| `data/experiment/tanda_final/t5/salidas/consola_columnas_tablero_t5.txt` | `5f455f9160f26183c789e3f94aa0f863c045cf02549c677f96fe72a0cd311ecd` |
| `data/experiment/tanda_final/t5/salidas/consola_contado_tramo1_t5.txt` | `31390a302f50cce2fa63a330399de4d87a7e7a4112ad21466d05e1f47f3db504` |
| `data/experiment/tanda_final/t5/salidas/consola_control_registro_tramo1_t5.txt` | `b1aa3ef54793ec216f87f48b5fba66c591743a47e5a12e2c8046711eca9d6cef` |
| `data/experiment/tanda_final/t5/salidas/consola_editar_grafos_t5.txt` | `2700b42c919ddf496a2310105eeefc4e049de28bbfefbb6872cbc2bc4b1e2a6d` |
| `data/experiment/tanda_final/t5/salidas/consola_no_abrir_t5.txt` | `e253ed5f6717d26fcbc012dc05ad793f36c496e376e506352a4b636884978731` |
| `data/experiment/tanda_final/t5/salidas/consola_reporte_t5.txt` | `655925949c0a05db43ae80839f0fce676c3922f13a733cacb9677a1957849054` |
| `data/experiment/tanda_final/t5/salidas/contado_tramo1_t5.json` | `fcd284096d4bc824335f0b39d66ffb1657fb288bfbf2ab746a52d9081984b34d` |
| `data/experiment/tanda_final/t5/salidas/control_registro_tramo1_t5.json` | `09b8a69973abd5107cd4a88dff7a2d87cbee3a97688520283383a03d53b265a5` |
| `data/experiment/tanda_final/t5/salidas/entrada_acumulado_60_t5.json` | `f5b561088c476459e38a824fa164607a97e8cbd65d702e9ce88aeaab3aadee90` |
| `data/experiment/tanda_final/t5/salidas/escritura_registro_tramo1_t5.json` | `9409366b10ccf1ce2c31abf0959e0b8d4e576020ed67d19d3cb2b4ab3805134c` |
| `data/experiment/tanda_final/t5/salidas/ids_modelo_t5.json` | `93fcd3a2d90183c914ef8528d61e769cec0c7578e4e11623c4804ed31822f7ce` |
| `data/experiment/tanda_final/t5/salidas/segunda_corrida/cifras_t5.json` | `17cb13d912e56c08c379e7e07e4a1ce4fa14f10620d3011b1ee1477a580553bb` |
| `data/experiment/tanda_final/t5/salidas/segunda_corrida/consola_cifras_t5_corrida2.txt` | `38c17182d8a2c602b9de57984351f814c4f7fe65fbe6a59fafe1b213e4ced688` |

**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `carpetas_tramo1_t5.py` | `0f492c6d6ba90b1a84dd5fcbfec8cb34603b078147e1018619071489a63321c0` |
| `cifras_t5_tf.py` | `dcdc441f82c61eb56877411eec6fa4c4c27c8730bc8497dacaf013639c3df445` |
| `columnas_tablero_t5.py` | `d46f254cb70039451813f59c2781c8cbb4dc008e3ac82fa90e3797c604c00b3a` |
| `contado_tramo1_t5.py` | `dca3d2b31fff81a244c78272c6545ee116addab4e1a0d548dfe6c945e0bcdfd1` |
| `control_registro_tramo1_t5.py` | `569d797be5182fd29b262719a5c4ba6496788e012488e251c06ad1e9e56b4b78` |
| `editar_grafos_t5.py` | `589d5453f5b66eb38bac9402ed5b02cd9daa80a5ec977b276243ea11ff389218` |
| `entrada_acumulado_60_t5.py` | `d506c837e8970fa94d562d00c5e843304ade6dad315ee01d4e83d99327e4637a` |
| `freno_t5_armar.py` | `8076089b7c2c0a65184fec183ff71df7de94175b6adf46a39fabe6ade06c079c` |
| `freno_t5_foto.py` | `970319d265d38e0bd3fa4239bd139390b09cc5b270db01f67a55b3cd3ce7f110` |
| `ids_modelo_t5.py` | `3faf74b46131c2c2b5279f3cb3faf4fd66b445f093e5c8ec2d62f9e12e9a4a27` |
| `no_abrir_t5.py` | `7c15a06e7064acd1b0d4551d00f4556237d1c350fef23faf4de230ea689b6a16` |
| `reporte_t5_tf.py` | `453da0796e5a5aa07dc54874bdd2fc9873d966c80ea5f4a56da2043f66a32b2e` |

- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los 34 archivos nuevos o cambiados de la foto, sin el `NO_ABRIR_`: 0 coincidencias, 0 archivos con rutas absolutas, 0 tokens dentro de rutas absolutas; control positivo, 2. Este FRENO y su script se escriben después de la foto: el control final del paquete confirma que son lo único nuevo y les pasa el grep.

## 12. El script de cada cifra

| cifras | script (`t5/scripts/`) | salida |
|---|---|---|
| el costo, los volúmenes, el tablero contra su meta, los hallazgos, las propuestas, el sello del tramo 1 | `cifras_t5_tf.py` | `salidas/cifras_t5.json` (y la segunda corrida) |
| los ids de modelo | `ids_modelo_t5.py` | `salidas/ids_modelo_t5.json` |
| el reporte y las propuestas | `reporte_t5_tf.py` | `reporte_tanda_final.md`, `propuestas_backlog_t5.jsonl` |
| las dos columnas del tablero | `columnas_tablero_t5.py` | las dos `*_PROPUESTA.md` |
| lo contado del tramo 1 | `contado_tramo1_t5.py`, `entrada_acumulado_60_t5.py` (sobre la copia) | `salidas/contado_tramo1_t5.json`, `salidas/entrada_acumulado_60_t5.json` |
| las carpetas del tramo 1 | `carpetas_tramo1_t5.py` | `salidas/carpetas_tramo1_t5.json` |
| el registro y su control | `editar_grafos_t5.py`, `control_registro_tramo1_t5.py` (sobre la copia) | `grafos.py`, la vista, `salidas/control_registro_tramo1_t5.json` |
| el `NO_ABRIR_` | `no_abrir_t5.py` | `NO_ABRIR_conteos_t5.json` |
| la foto | `freno_t5_foto.py` | la sección 11 |
| este FRENO | `freno_t5_armar.py` | este archivo |
| el paso 0 | `paso0_t5.sh` y sus tres scripts, en el paquete | su salida, pegada |

Los adaptadores que escribieron `contado_tramo1_t5.py`, `editar_grafos_t5.py`, `control_registro_tramo1_t5.py` y `freno_t5_foto.py` desde los de T3 y T4, con reemplazos exactos, van en el paquete.

## 13. Errores propios, con su causa

1. **La salida del paso 0 imprime filtrada la comparación de la foto.** En `paso0_t5.sh`, un `grep -v` sacaba de la impresión los renglones que empiezan con una ruta, y con ellos las rutas de las listas. La comparación y su JSON están completos; la sección 1 da las listas desde el JSON. No lo vi hasta leer la salida.
2. **La primera corrida de lo contado del tramo 1 no arrancó** (rc 127): en una subshell con `cd` a la copia, `$PWD` ya era la copia y el intérprete no estaba ahí. No corrió nada; la relancé con la ruta absoluta.
3. **Tres scripts frenaron en su primera corrida, sin escribir:** `ids_modelo_t5.py` (las listas de TOs de los tramos son diccionarios), `cifras_t5_tf.py` (leía mal «USD 0,209440,») y `freno_t5_foto.py` (el `NO_ABRIR_` no tiene sha256 en la foto). Los corregí y volví a correr. En `cifras_t5_tf.py` cambié además una etiqueta antes de las dos corridas, que rehice enteras.
4. **Saqué la foto de después cuatro veces** (14:01:00, 14:01:53, 14:05:02 y 14:05:57). Cada una de las tres primeras quedó vieja porque después cambié un archivo de `t5/`: primero corregí `freno_t5_foto.py` (fallaba con el `NO_ABRIR_`, que no tiene sha256 en la foto); después, el formato de tres cifras de los hallazgos en `cifras_t5_tf.py`, y con él `cifras_t5.json` y el reporte; y por último otra vez `freno_t5_foto.py`, que buscaba la hora de un `.DS_Store` que agregó Finder y la foto no la guarda. Las borré. Los sha256 de la segunda y la tercera están en `sha_fotos_despues_descartadas_T5.txt`, en el paquete; el de la primera no: lo anoté en un archivo de la carpeta de trabajo que borré al rehacerla. La sección 11 es la de la cuarta.
5. **La sección 11 dice «tamaño en bytes y hora» del `NO_ABRIR_` y da solo el tamaño.** El texto viene del script de T4 y no lo corregí para no sacar la foto una cuarta vez.
6. **Un control de un adaptador frenó antes de escribir:** el de `freno_t5_foto.py` buscaba `GRAFOS` donde el script dice `GRUPOS`.

## 14. Lo que no hice

- **La señal cid, el material del catálogo ni nada de la clasificación del freno.**
- **No escribí** en el tablero, el backlog, la tabla de reprocesamiento ni el registro de decisiones; no re-ensamblé ni toqué los grafos, los manifiestos, la E0, el código del pipeline, la fixture, el registro de alcance ni nada de `t1/` a `t4/`. Fuera de `t5/`, solo las dos entradas de `grafos.py`.
- **No cargué nada en Neo4j.**
- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en `.gitignore`.
- **El scratchpad:** nada que se necesite después queda solo en él; las fotos van a `t4t2_fotos/` y el resto, al paquete.
- Los heredocs, siempre con el delimitador entre comillas.

FRENO T5: espero la revisión de la mesa.
