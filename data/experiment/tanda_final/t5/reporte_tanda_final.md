# Reporte de cierre de la tanda final de B6.1 (T5)

Pre-registro de la tanda final, firmado en `4de7f2a7` (§5 y §7), con sus notas al pie (`27bfaeb5` y `86541475`); enmienda 9 al protocolo entre tandas (`756a0394`), §1, punto 1; el protocolo entre tandas, §2, y el pre-registro de la tanda 1, §5.6, para los hallazgos. Toda cifra sale de `t5/salidas/cifras_t5.json` (`t5/scripts/cifras_t5_tf.py`); este archivo lo arma `t5/scripts/reporte_t5_tf.py`. USD 0, sin API.

## 1. Los volúmenes

#### Tabla 1. Las unidades por tramo (`volumenes`, de `t2/resumen_t2_final.json`)

| tramo | TOs | unidades | con las partes | aceptadas (los tres estados juntos) | cola | errores definitivos | sin destino | ids repetidos |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tramo 1 | 30 | 601 | 601 | 587 | 13 | 1 | 0 | 0 |
| tramo 2 | 68 | 4.350 | 4.350 | 4.283 | 67 | 0 | 0 | 0 |
| tanda final | 98 | 4.951 | 4.951 | 4.870 | 80 | 1 | 0 | 0 |

El error definitivo está en ri_transpa (la unidad muda de la fila 61 del tablero; hallazgo H-T5-01).

#### Tabla 2. Los ocho ensamblados de T3 (`volumenes.ensamblados`, de `t3/salidas/doble_corrida_tf.json`)

| grafo | nodos | aristas | sha256 del `kg.json` | dos corridas iguales |
|---|---:|---:|---|---|
| KG-Acumulado-Tandas0y1yFinal-r2b | 38.324 | 114.925 | `c43d66e503c2b27477cd17a5ffc2c64b6334d9525f0524d82ff248f04e7d96ac` | sí |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | 37.321 | 104.279 | `398459a853590c584398243b543548d5634124d5577b3cfffe4332f0a61ac0fd` | sí |
| KG-TandaFinal-r2b | 17.025 | 46.273 | `db2df7b7e707ef191d1df6fdb3638fd920cf4486afce13a7e889b9755155bc97` | sí |
| KG-TandaFinal-r2b-sincola | 16.598 | 43.392 | `c050f3c90ce5d32be759d2e5d05bbe2e131d9abf7811de097c97f4a1fe410cf7` | sí |
| KG-Acumulado-Tandas0y1yTramo1-r2b | 23.671 | 67.006 | `87ea32c503cd79bcf537a5d259527f4a50ccf00dc40a682ea9abc200b8d6ce50` | sí |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | 22.930 | 59.354 | `4ec19d46f23b80866866e132d6d367b88f9f83c12856abba36536ad06dd9d32d` | sí |
| KG-TandaFinal-Tramo1-r2b | 2.372 | 4.066 | `f064d4e00b41246525d3c30a88f33b3ba9672c5e02cc10a36a4fa18dc88b940c` | sí |
| KG-TandaFinal-Tramo1-r2b-sincola | 2.207 | 3.822 | `bbda74cda7e071e27782b41b06d7557e2c153e8afff7ea3f6540bdd520c3615f` | sí |

## 2. El costo real contra el estimado (§3 y §7)

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

## 3. Los ids de modelo que devolvió la API (`ids_de_modelo`, de `t5/salidas/ids_modelo_t5.json`)

| etapa | ids | llamadas | lo esperado | igual |
|---|---|---|---|---|
| E1 | claude-haiku-4-5-20251001 | claude-haiku-4-5-20251001: 4.997 | claude-haiku-4-5-20251001 | sí |
| reintentos de E1 de la fase de E3 | claude-haiku-4-5-20251001 | en el `NO_ABRIR_` | claude-haiku-4-5-20251001 | sí |
| E3 | claude-sonnet-5 | en el `NO_ABRIR_` | claude-sonnet-5 | sí |

Lo esperado sale del pre-registro de la tanda final, §2; no nombra ids de modelo; los esperados salen del pre-registro de la tanda final, §2. El freno por modelo de T2: OK, con claude-haiku-4-5-20251001 en E1 y claude-sonnet-5 en E3 (t2/FRENO_T2.md, resultado).
Las llamadas de E1 incluyen sus reintentos y las partes; las de E3 cuentan los reintentos de E3 y van solo al `NO_ABRIR_`.

## 4. Las incidencias

- **T1** (`t1/FRENO_T1.md`): la corrida en seco frenó con dos decisiones para la autora antes de T2: el estimado por TO del manifiesto, que pasó a ser el repartido por caracteres (nota al pie `27bfaeb5`), y si el ensamblado del tramo 1 alcanzaba para su sello. Hubo además un incidente externo (un Neo4j que se apagó y reescribió su volumen, ignorado por git).
- **T2** (`t2/FRENO_T2.md`): el control entre tramos dio FRENO por 1 error definitivo en el tramo 1 (ri_transpa); con la decisión de la autora, el segundo lanzamiento siguió con el tramo 2 y terminó con salida 0. La unidad falta en los grafos, como decidió la autora (registro de decisiones, §44); su causa está en `BKL-0050`.
- **T3** (`t3/FRENO_T3.md`, §2): el selftest de claves sin la R23 y la V23; los manifiestos del tramo 1 con la raya (enmienda 9, punto 8); el derivador adaptado del acumulado de 60; los umbrales de T4 del script de la mesa; y la lista de unidades a la vista. Las regresiones declaradas del gate van en los hallazgos (H-T5-08).
- **La regla de las dudosas** (pre-registro, §6; registro, §35): una «dudosa» cuenta como error para la tasa, la atención y el freno, y la cuenta sin ellas va al lado como sensibilidad. En T4 no hubo dudosas en la cola ni en las aceptadas.

## 5. Las tasas de T4 (`t4/tasas/tasas_t4_tramo3.json`)

La tabla 1 de `t4/tablas_t4_tramo3.md` (de `t4/scripts/tablas_t4t3_tf.py`), tal cual:

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |
|---|---|---|---|---|---|
| aceptadas, ítems | 6 de 30 (6 con error y 0 dudosas); ponderada 0,2862, Wilson [0,1090; 0,5678] (n ef. 11,888); sin las dudosas, 6 de 30, 0,2862 [0,1090; 0,5678] | 9 de 30 con las dudosas como error; ponderada 0,2196, Wilson de Kish [0,0784; 0,4822]; atención: no; freno: no | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,2710); freno: no | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas.items` |
| aceptadas, no ítems, sobre las 60 | 16 de 60 (16 con error y 0 dudosas); ponderada 0,3733, Wilson [0,2160; 0,5630] (n ef. 26,266); sin las dudosas, 16 de 60, 0,3733 [0,2160; 0,5630]; sobre las 30 del primer tramo, 7 de 30, 0,3674 | 3 de 30 con las dudosas como error; ponderada 0,0968, Wilson de Kish [0,0214; 0,3446]; atención: no; freno: no | 4 de 30, Wilson [0,0531; 0,2968] | atención sobre las 30: sí (p 0,0168); freno por la atención sobre las 60: sí (umbral 0,2437, p 0,0009); freno por intervalos: no | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas_no_items_sobre_60` y `aceptadas.no_items` |
| aceptadas, ponderada total | con las 30 de no ítems, 0,3458, Wilson [0,1819; 0,5570] (n ef. 21,260); sin las dudosas, 0,3458 [0,1819; 0,5570]; con las 60 de no ítems (información), 0,3502, Wilson [0,2185; 0,5097] (n ef. 37,773) | 0,1397, Wilson de Kish [0,0532; 0,3196] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `aceptadas.total` |
| atención de RI | con las 30 de no ítems, 5 de 30; ponderada de RI 0,1843, Wilson [0,0661; 0,4191] (n ef. 16,967); sin las dudosas, 5 de 30, 0,1843; con las 60 de no ítems (información), 8 de 45, 0,1843, p 0,2339 | 7 de 30; ponderada de RI 0,1747; la atención no salta | bajo H0, 0,1433 (umbral de T3: 0,2918) | atención: no (p 0,2945) | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `atencion_RI` |
| tasa de error de la cola | 12 de 30 (12 con error y 0 dudosas); ponderada 0,3706, Wilson [0,2057; 0,5723] (n ef. 23,100); sin las dudosas, 12 de 30, 0,3706 [0,2057; 0,5723] | 14 de 30 con las dudosas como error; ponderada 0,4386, Wilson de Kish [0,2751; 0,6166]; la regla del 25 % se dispara | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `cola` |
| observación (12) | 29 correctas de 30 (0 no decidibles, en el denominador; 1 incorrecta: catálogo 1); Wilson [0,8333; 0,9941]; ponderada por celda 0,9934 [0,7576; 0,9999] | 27 correctas de 30, Wilson [0,7438; 0,9654] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro de la tanda 1, §5.2, como lo da tanda1/t4/scripts/tasas_t4t2.py) | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `observacion:12` |
| vigilancia (1) | 7 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,2333, Wilson [0,1179; 0,4093]; ponderada por celda 0,2010 [0,0627; 0,4858] | 3 sí de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 6 vaciamientos de 30; cruda 0,2000, Wilson [0,0951; 0,3731]; ponderada por celda 0,1483 [0,0516; 0,3579] | 15 vaciamientos de 30 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 5 duplicaciones de 30; cruda 0,1667, Wilson [0,0734; 0,3356]; ponderada por celda 0,1670 [0,0522; 0,4218] | 9 duplicaciones de 30 | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 6; cruda 0,3333, Wilson [0,0968; 0,7000]; leída entera, sin celdas | 2 sin apoyo de 4 | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t3_tf.py`, `tasas/tasas_t4_tramo3.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, sí; la de RI, no. Hay ampliación: sí. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items sí, RI no.
- **Las aceptadas no ítems sobre las 60** (las 30 del primer tramo y las 30 de la ampliación; cada celda con el doble: sí): freno por la atención sobre las 60, sí; freno por intervalos, no. Con las dudosas fuera, la sensibilidad da otra decisión: no. Su fila de la hoja es la de las 60 (tablas 10 y 11).
- **La ponderada total y la atención de RI con las 60** van como información, sin decisión, al lado de las del segundo tramo (tabla 12).
- **Las líneas de base:** la tanda 1, los valores T4.* de tanda_final/preregistro/preregistro_tanda_final_derivada_T4.huecos.json (versión derivada para la lectura); la tanda 0, al lado, la de cada fila de `lineas_de_base`.
- **Los controles de la entrada** (`scripts/tasas_t4t3_tf.py`): 48 de 48 pasan.
- **Lo del segundo tramo da lo mismo** (`lo_del_segundo_tramo`): 9 de 9 bloques iguales a `tasas/tasas_t4_tramo2.json`; en las líneas de base cambian solo `aceptadas:total.tanda0` y `atencion_RI.tanda0`.

- **El freno de las aceptadas no ítems:** la atención sobre las 60 se confirma (tasa 0,3733, umbral 0,2437, p 0,0009); el freno por intervalos, no.
- Lo que sigue al freno lo decide la autora con su clasificación (registro de decisiones, §89).

## 6. La columna «Tanda final» del tablero

Va completa, como propuesta, en `t5/columna_tanda_final_tablero_PROPUESTA.md` (de `t5/scripts/columnas_tablero_t5.py`): las celdas de T3 y la fila 59, que esperaba a T4. El tablero del repo no se toca. Cada fila contra su meta (`tablero_contra_su_meta`):

| fila | síntoma | cifra | estado | criterio |
|---:|---|---|---|---|
| 49 | **Observación (10):** extracción más magra | 5,18 aristas de extracción por unidad | sin meta numérica | la meta dice «Sin meta numérica»: la cifra se vigila como descriptivo |
| 50 | **Observación (11):** menos remisiones entre documentos | 4001 `remite_a` entre documentos | no se decide con lo contado | la meta es de precisión (toda `remite_a` sostenida por cita y destino) y la lectura de T4 no la mide aparte |
| 51 | **Aristas `referencia` por tipo de origen:** ninguna sale de Condicion, Potestad ni Definicion | 0 `referencia` con origen distinto de TextoOrdenado | cumple | ninguna `referencia` sale de Condicion, Potestad ni Definicion |
| 52 | **Condiciones sin regla** (antes «Condiciones aisladas»; redefinida por decisión de la autora del 07/10/2026) | 0 Condicion sin ninguna arista; 331 sin regla de 2247, declaradas por causa; aislados 34 (Comunicacion 32, Sujeto 2) | cumple | la parte medible de la meta, cero Condicion sin `establecida_en` ni ninguna arista, da 0; las sin regla se declaran por causa. Los aislados no son Condicion |
| 53 | **Remisiones falsas por paráfrasis** | acumulado de las tres: 0 hacia cap 6.5.1 o debajo | cumple | la tanda no tiene cap; se mide en el acumulado |
| 54 | **Test del ejemplo `cla::5.1.1.1`** | acumulado de las tres: resuelto | cumple | la tanda no tiene cla; se mide en el acumulado |
| 55 | **Regresiones de la suite contra r1** | no declaradas que cuentan: tanda 0, acumulado 0; declaradas: laudo 3, autora 2 | cumple | 0 regresiones que cuentan en el gate; las declaradas, aparte (hallazgos) |
| 56 | **Patrón de navegación (a):** ancla vista por `referencia` sin abrir | no medido | residuo declarado | la meta declara el residuo: no medible en r2 sin correr el agente |
| 57 | **Patrón de navegación (b):** vecinos solo salientes sobre una Operacion con restricciones entrantes | no medido | residuo declarado | la meta declara el residuo: no medible en r2 sin correr el agente |
| 58 | **Tope de herramientas alcanzado** | no medido | residuo declarado | la meta declara el residuo: no medible en r2 sin correr el agente |
| 60 | **Clases de falla A0.2** | no medido | residuo declarado | la meta declara el residuo: no medible en r2 sin correr el agente |
| 59 | **Incorrectas de la observación (12), por capa** | 29 correctas de 30; 1 incorrecta (catálogo) | no cumple | la meta cerró la fila con la precisión de L2; una incorrecta de la lectura es un hallazgo (protocolo, §2) |
| 61 | **Unidades cortadas o mudas** | 1 de 4951 | no cumple | la meta pide cero unidades con error definitivo por corte y M10 en 0 |
| 62 | **Afirmación falsa por tabla no detectada (`cap::1.2`, `BKL-0006`)** | acumulado: BKL-0006 resuelto, BKL-0023 resuelto | cumple | la tanda no tiene cap; la meta pide BKL-0006 y BKL-0023 aplicables y en «resuelto» |
| 63 | **Pérdidas de contenido por tablas** | acumulado: 5 de 5 citas presentes | cumple | la tanda no tiene los TOs de las citas; se mide en el acumulado |
| 64 | **Valores fuera de lista cerrada** | sin marca ni original: Restriccion.tipo 0, Comunicacion.tipo 85, Obligacion.tipo 0, Obligacion.frecuencia 0; claves fuera 0 | cumple, con el residuo que la meta declara | fuera de lista sin tratar = sin marca y sin el original guardado; la meta declara como residuo de r2b la Comunicacion sin `tipo` |
| 65 | **Mención del sujeto sin guardar; sujetos no mapeables** | 6050 de 6050 con mención | cumple | toda relación con sujeto lleva su mención |
| 66 | **Catálogo de sujetos en dos fuentes** | 0 / 0 | cumple | una sola fuente: 0 / 0 |
| 67 | **Cuantías sin campo estructurado** | 14 sin campo de 1297 con cuantía (Condicion 2, Obligacion 12) | no cumple | toda cuantía con elemento de umbral o con marca; el residuo que la meta declara es el de diez |
| 68 | **Omisiones sin registro fuera de los chunks marcados** | sin categoría 0, sin tramo 1 | cumple | toda omisión con categoría y tramo; la meta declara un residuo de 1 sin tramo por grafo |
| 69 | **Crudo del reintento de E3 sin persistir** | en t3/NO_ABRIR_conteos_t3.json | no se decide: bajo el cegamiento | usa los reintentos de E3 |
| 70 | **Colisiones de ids de chunk en E0 (`BKL-0037`)** | 0 | cumple | 0 ids repetidos |
| 71 | **Relaciones de la matriz ampliada sin verificar por E3** (`condicion_de` → Operacion y → Potestad) | 0 | cumple | 0 sin verificar por E3 |
| 72 | **Líneas en mayúsculas descartadas al tope de la página (E0 legada)** | no medido | no aplica | la fila lee la E0 legada, que la tanda final no tiene |
| 73 | **Pies de página dentro del texto de E0** | 0 de 4951 | cumple | 0 chunks con pie |
| 74 | **Plazos sin cuantía mandados a `frecuencia`** | 0 a `frecuencia` | cumple | 0 plazos sin cuantía mandados a `frecuencia` |

## 7. Los hallazgos, en los ejes A y B

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

## 8. Lo que sigue (no lo hace T5)

- **La señal cid:** las 3 unidades de la tanda final con «(cid:», después de su T5 (registro de decisiones, §14).
- **El catálogo al cierre:** su material, con la decisión 4 del §9 del pre-registro, después del sello.
- **La clasificación del freno** de las aceptadas no ítems, que hace la autora (registro de decisiones, §89).
