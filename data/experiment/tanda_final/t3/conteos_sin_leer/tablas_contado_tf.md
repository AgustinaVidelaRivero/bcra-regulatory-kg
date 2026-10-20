#### Tabla C1. Observaciones (10) y (11) contra la tanda 1, con la tanda 0 re-sellada al lado

| grafo | unidades de E0 | (10) aristas de extracción | (10) por unidad | (11) `remite_a` entre documentos | menciones |
|---|---:|---:|---:|---:|---:|
| tanda final | 4.951 | 25.629 | 5,18 | 4.001 | 2.517 |
| tanda final sin cola | 4.951 | 24.949 | 5,04 | 2.520 | 2.408 |
| acumulado de las tres | 10.680 | 57.767 | 5,41 | 16.180 | 5.311 |
| acumulado de las tres sin cola | 10.680 | 56.297 | 5,27 | 10.236 | 5.117 |
| base de la tanda 1: tanda 1 | 3.290 | 18.887 | 5,74 | 1.541 | 1.272 |
| base de la tanda 1: tanda 1 sin cola | 3.290 | 18.483 | 5,62 | 299 | 1.224 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 5.729 | 32.138 | 5,61 | 3.628 | 2.783 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | 5.729 | 31.348 | 5,47 | 2.061 | 2.698 |
| base re-sellada: diez | 2.439 | 13.251 | 5,43 | 642 | 1.510 |
| base re-sellada: desarrollo | 1.768 | 10.304 | 5,83 | 497 | 1.289 |

#### Tabla C2. Vigilancias (4), (5), (8) y (9) contra la tanda 1, con la tanda 0 re-sellada al lado

| grafo | (4) un TextoOrdenado por TO | (5) requisito_de_estructura / normalizados | (8) sujeto_propuesto / sujeto_id (tasa %) | (9) emisiones en E1 / aristas en el kg |
|---|---|---|---|---|
| tanda final | True | 0 / 0 | 579 / 5.365 (9,74) | 22 / 33 |
| tanda final sin cola | True | 0 / 0 | 579 / 5.365 (9,74) | 22 / 33 |
| acumulado de las tres | True | 0 / 1 | 1205 / 11.665 (9,36) | 29 / 59 |
| acumulado de las tres sin cola | True | 0 / 1 | 1205 / 11.665 (9,36) | 29 / 59 |
| base de la tanda 1: tanda 1 | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| base de la tanda 1: tanda 1 sin cola | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base re-sellada: diez | True | 0 / 0 (los diez TOs) | 192 / 2.350 (7,55) | 0 (los diez TOs) / 8 |
| base re-sellada: desarrollo | True | 0 / 0 (los diez TOs) | 138 / 1.641 (7,76) | 0 (los diez TOs) / 8 |

#### Tabla C3. La cola, contra la de la tanda 1, con la tanda 0 re-sellada al lado

| grafo | cola | de unidades de E0 | % | por estado | aceptadas (los tres estados juntos) | en el grafo |
|---|---:|---:|---:|---|---:|---|
| tanda final | 80 | 4.951 | 1,6 | cola_humana 20, cola_humana_reextraccion_invalida 9, cola_humana_veredicto_inutilizable 51 | 4.870 | 499 nodos y 679 aristas con la marca |
| tanda final sin cola | 80 | 4.951 | 1,6 | cola_humana 20, cola_humana_reextraccion_invalida 9, cola_humana_veredicto_inutilizable 51 | 4.870 | 80 descartadas por el ensamblado |
| acumulado de las tres | 191 | 10.680 | 1,8 | cola_humana 63, cola_humana_reextraccion_invalida 13, cola_humana_veredicto_inutilizable 115 | 10.493 | 1123 nodos y 1472 aristas con la marca |
| acumulado de las tres sin cola | 191 | 10.680 | 1,8 | cola_humana 63, cola_humana_reextraccion_invalida 13, cola_humana_veredicto_inutilizable 115 | 10.493 | 191 descartadas por el ensamblado |
| base de la tanda 1: tanda 1 | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | — |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | — |
| base re-sellada (diez) | 69 | 2.439 | 2,8 | cola_humana 25, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 42 | — | — |

El umbral de atención es 6 % (§5.4 b). Las unidades en `finales.jsonl` son tanda final 4.950, tanda final sin cola 4.950, acumulado de las tres 10.684, acumulado de las tres sin cola 10.684 (las partes por corte cuentan aparte); otros estados: tanda final ninguno, tanda final sin cola ninguno, acumulado de las tres ninguno, acumulado de las tres sin cola ninguno.

La cola por TO (tanda final): adfsp 1, afiltr 1, apnf 1, autenf 3, cateloc 3, cedin 1, cescar 2, consyr 2, cryl 1, ctavis 4, depinv 2, disres 3, evacre 1, fabcra 2, fimipyme 2, finsec 6, garopt 1, gescre 1, gracre 1, graloc 1, jafip 2, lavdin 1, pimf 1, prevmi 1, raapal 2, ratio 5, ratiofn 3, regpri 4, repefe 1, retype 1, ri_dsf 2, ri_iepsp 1, ri_ii_31_12_19 1, ri_msrl 2, ri_secoexpo 1, ri_tar 1, rmgcti 1, secfin 2, seggar 2, servco 1, snp_cec 3, snp_spd 1, tasint 1, traval 1.

#### Tabla C4. El catálogo al cierre (§5.5): claves con la mención verificada en cuarentena en 2 unidades o más

| registro | filas en cuarentena | verificadas | claves | claves con 2 unidades o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|
| tanda final | 1088 | 956 | 303 | 45 | 19 |
| tanda final sin cola | 1055 | 924 | 297 | 43 | 19 |
| acumulado de las tres | 1939 | 1669 | 588 | 108 | 47 |
| acumulado de las tres sin cola | 1894 | 1626 | 577 | 105 | 47 |
| base de la tanda 1: tanda 1 | 703 | 570 | 237 | 38 | 8 |
| base de la tanda 1: tanda 1 sin cola | 693 | 561 | 233 | 37 | 8 |
| base de la tanda 1: acumulado de las tandas 0 y 1 | 851 | 713 | 320 | 56 | 13 |
| base de la tanda 1: acumulado de las tandas 0 y 1 sin cola | 839 | 702 | 315 | 54 | 12 |
| base de la tanda 0: diez (r2_1_medicion.json) | 164 | 145 | 87 | 14 | 1 |
| base de la tanda 0: diez_sincola (r2_1_medicion.json) | 162 | 143 | 85 | 14 | 1 |

Las claves y sus formas están en `contado_sin_leer_tf.json` (`catalogo_al_cierre`). Su lectura y aprobación es de la autora (enmienda 4, §1, punto 3); cuántas relaciones resuelve cada versión del catálogo se mide después de la re-resolución (punto 5).

Control de las funciones importadas: las del re-sellado sobre KG-Tanda0-Diez-r2b-rs1 contra su medición, True en las 11 filas controladas; las de este script sobre KG-Tanda1-Veinte-r2b-sincola contra la línea de base de la tanda 1, True en las 5 filas controladas. Los pozos de L-02 y L-04 no se miden: eran de la lectura de la tanda 1 (su pre-registro, §5.4 d).
