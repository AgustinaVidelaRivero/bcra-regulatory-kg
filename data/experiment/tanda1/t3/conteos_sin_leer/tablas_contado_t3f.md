#### Tabla C1. Observaciones (10) y (11) contra sus líneas de base re-selladas (pre-registro, §5.2)

| grafo | unidades de E0 | (10) aristas de extracción | (10) por unidad | (11) `remite_a` entre documentos | menciones |
|---|---:|---:|---:|---:|---:|
| veinte | 3.290 | 18.887 | 5,74 | 1.541 | 1.272 |
| veinte sin cola | 3.290 | 18.483 | 5,62 | 299 | 1.224 |
| acumulado | 5.729 | 32.138 | 5,61 | 3.628 | 2.783 |
| acumulado sin cola | 5.729 | 31.348 | 5,47 | 2.061 | 2.698 |
| base re-sellada: diez | 2.439 | 13.251 | 5,43 | 642 | 1.510 |
| base re-sellada: desarrollo | 1.768 | 10.304 | 5,83 | 497 | 1.289 |

#### Tabla C2. Vigilancias (4), (5), (8) y (9) contra sus líneas de base re-selladas (§5.3)

| grafo | (4) un TextoOrdenado por TO | (5) requisito_de_estructura / normalizados | (8) sujeto_propuesto / sujeto_id (tasa %) | (9) emisiones en E1 / aristas en el kg |
|---|---|---|---|---|
| veinte | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| veinte sin cola | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| acumulado | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| acumulado sin cola | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base re-sellada: diez | True | 0 / 0 (los diez TOs) | 192 / 2.350 (7,55) | 0 (los diez TOs) / 8 |
| base re-sellada: desarrollo | True | 0 / 0 (los diez TOs) | 138 / 1.641 (7,76) | 0 (los diez TOs) / 8 |

#### Tabla C3. La cola (§5.4 b), contra los 69 de 2.439 del re-sellado

| grafo | cola | de unidades de E0 | % | por estado | aceptadas (los tres estados juntos) | en el grafo |
|---|---:|---:|---:|---|---:|---|
| veinte | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | 313 nodos y 408 aristas con la marca |
| veinte sin cola | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | 42 descartadas por el ensamblado |
| acumulado | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | 627 nodos y 793 aristas con la marca |
| acumulado sin cola | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | 111 descartadas por el ensamblado |
| base re-sellada (diez) | 69 | 2.439 | 2,8 | cola_humana 25, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 42 | — | — |

El umbral de atención es 6 % (§5.4 b). Las unidades en `finales.jsonl` son veinte 3.294, veinte sin cola 3.294, acumulado 5.734, acumulado sin cola 5.734 (las partes por corte cuentan aparte); otros estados: veinte ninguno, veinte sin cola ninguno, acumulado ninguno, acumulado sin cola ninguno.

La cola por TO (veinte): cajasc 3, cirmo3 2, depaho 6, efemin 3, lingeef 10, manori 4, ri_ccna 6, ri_dcpc 1, ri_pgn 1, ri_rml 3, snp_cheq 1, snp_tr 2.

#### Tabla C4. El catálogo al cierre (§5.5): claves con la mención verificada en cuarentena en 2 unidades o más

| registro | filas en cuarentena | verificadas | claves | claves con 2 unidades o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|
| veinte | 703 | 570 | 237 | 38 | 8 |
| veinte sin cola | 693 | 561 | 233 | 37 | 8 |
| acumulado | 851 | 713 | 320 | 56 | 13 |
| acumulado sin cola | 839 | 702 | 315 | 54 | 12 |
| base de la tanda 0: diez (r2_1_medicion.json) | 164 | 145 | 87 | 14 | 1 |
| base de la tanda 0: diez_sincola (r2_1_medicion.json) | 162 | 143 | 85 | 14 | 1 |

Las claves y sus formas están en `contado_sin_leer_t3f.json` (`catalogo_al_cierre`). Su lectura y aprobación es de la autora (enmienda 4, §1, punto 3); cuántas relaciones resuelve cada versión del catálogo se mide después de la re-resolución (punto 5).

#### Tabla C5. Los pozos de L-02 y L-04 (§5.4 d; cegamiento, punto 8: solo si llegan a 30)

- L-02 (detecciones de la tanda 1 (veinte, con la cola)): llega a 30: True.
- L-04 (nodos Comunicacion con `tipo_no_derivable`): veinte llega a 30: True; veinte sin cola llega a 30: True.
- Las cuentas, en `NO_ABRIR_conteos_t3.json`.

Control de las funciones importadas (las del re-sellado sobre KG-Tanda0-Diez-r2b-rs1 contra su medición): True en las 11 filas controladas.
