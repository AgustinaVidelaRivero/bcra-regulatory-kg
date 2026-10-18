#### Tabla V0. La E0 con las partes (`gate_decisiones/e0_con_partes_t3f.json`)

| E0 | archivos | dos corridas iguales | sha256 del conjunto |
|---|---:|---|---|
| tanda1 | 107 | True | `f079c1ff1b680eb7c766e8bebf05da489f474dd39e68ad228266296e8bd52028` |
| acumulado | 150 | True | `a9ff9b7b6e6228ca1db6dbcfebd63894e7d57e3c95d0652b7c47a4d981667c05` |

El acumulado rearmado en la copia, igual al del repo: True; su entrada, 557 archivos y 297695212 bytes.

#### Tabla V1. El control de shapes con esa E0, contra el FRENO parcial (`gate_decisiones/e0_con_partes_t3f.json`, `shapes`)

| grafo | archivo | byte a byte | líneas del diff crudo | igual con rutas y fecha normalizadas | control |
|---|---|---|---:|---|---|
| ens_veinte_r2b | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_veinte_r2b | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_veinte_r2b | consola_shapes.txt | True | 0 | True | True |
| ens_veinte_r2b_sincola | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_veinte_r2b_sincola | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_veinte_r2b_sincola | consola_shapes.txt | True | 0 | True | True |
| ens_treinta_r2b | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_treinta_r2b | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_treinta_r2b | consola_shapes.txt | True | 0 | True | True |
| ens_treinta_r2b_sincola | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_treinta_r2b_sincola | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_treinta_r2b_sincola | consola_shapes.txt | True | 0 | True | True |

#### Tabla V2. El veredicto del gate por grafo

| grafo | shapes, E0 con las partes (rige) | shapes, E0 del repo (informada) | suite: resuelto / persiste / no aplica | regresiones | declaradas (laudo) | declaradas (autora) | fuera del grafo | no declaradas que cuentan |
|---|---|---|---|---:|---:|---:|---:|---|
| veinte | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 31 / 16 / 21 | 20 | 3 | 2 | 18 | 0 |
| veinte_sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 31 / 16 / 21 | 20 | 3 | 2 | 18 | 0 |
| acumulado | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| acumulado_sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |

Las columnas de shapes dan PASS / FAIL / WARN. «Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo no tiene; en el acumulado no se aplica (decisión 3). Las declaradas del laudo, en la tanda 1 sola, también caen fuera del grafo.

- **veinte, «fuera del grafo»:** 18 regresiones (BKL-0001, BKL-0002, BKL-0005, BKL-0006, BKL-0023, EJ-cla-5.1.1.1, ID-alta_gerencia, ID-comite_de_auditoria, ID-directorio, RT-C5-3, RT-C6-1, RT-C6-2, RT-C7-1, RT-C7-2, RT-C7-3, T1, T2, T3); de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con `clasificar_regresiones_t3.py`: 15 y 15 ítems, iguales: True.

- **veinte_sincola, «fuera del grafo»:** 18 regresiones (BKL-0001, BKL-0002, BKL-0005, BKL-0006, BKL-0023, EJ-cla-5.1.1.1, ID-alta_gerencia, ID-comite_de_auditoria, ID-directorio, RT-C5-3, RT-C6-1, RT-C6-2, RT-C7-1, RT-C7-2, RT-C7-3, T1, T2, T3); de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con `clasificar_regresiones_t3.py`: 15 y 15 ítems, iguales: True.

#### Tabla V3. Reproducibilidad, selftests, intrínsecas y contadores (de las tablas 2, 6, 7 y 8 del FRENO parcial)

- **Reproducibilidad:** 6 cadenas, todas iguales: True; veredicto OK.
- **Selftests:** catalogo_unico rc=1, catalogo_unico_en_clon_git rc=0, clave_cache rc=0, e0 rc=0, ensamblado_omisiones rc=0, metrica_condiciones rc=0, pyd_r2 rc=0, r3 rc=0, regression_kg_1 rc=0, regression_kg_2 rc=0, shapes_congelado rc=0; el de claves, OK. El del catálogo pide git: rc=1 en la copia y rc=0 en el clon de git del parcial (error propio 1, declarado por la decisión 7).
- **Intrínsecas de generación 3, con la E0 con las partes (informativas):**
  - KG-Tanda1-Veinte-r2b: M4 4.945095, M9 16 nodos aislados, M10 0 / 3294.
  - KG-Tanda1-Veinte-r2b-sincola: M4 4.548667, M9 16 nodos aislados, M10 42 / 3294.
  - KG-Acumulado-Tandas0y1-r2b: M4 5.626325, M9 23 nodos aislados, M10 0 / 5734.
  - KG-Acumulado-Tandas0y1-r2b-sincola: M4 5.314453, M9 23 nodos aislados, M10 111 / 5734.
- **Contadores de E1 (informativos):** {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 1}.

**Veredicto del gate, con las decisiones 1 a 3: PASA.**
