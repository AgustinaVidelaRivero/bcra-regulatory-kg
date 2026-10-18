# Reporte de cierre de la tanda 1 de B6.1

Pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota al pie en `ca5b39fd`): §3 («Al cerrar»), §5.5,
§5.6 y el §6 donde se cita. USD 0, sin API. Lo genera `t5/scripts/reporte_t5.py` desde las salidas de `t5/scripts/cifras_t5.py` y
`t5/scripts/selftest_t5.py`; cada cifra va con la salida de la que se copia. Las aclaraciones que no son cifras de una salida son de
la ejecutora de T5 y lo dicen.

## 1. Los volúmenes

De `t5/salidas/volumenes_t5.json` (de `t2/resumen_t2.json` y `t3/salidas/doble_corrida_t3.json`).

| unidades | con las partes por corte | aceptadas (los tres estados juntos) | cola | errores | ids repetidos |
|---:|---:|---:|---:|---:|---:|
| 3.290 | 3.294 | 3.252 | 42 | 0 | 0 |

| grafo | unidades de E0 | nodos | aristas | sha256 del `kg.json` |
|---|---:|---:|---:|---|
| KG-Tanda1-Veinte-r2b | 3.290 | 12.731 | 31.478 | `22e83a62cb88e5bb…` |
| KG-Tanda1-Veinte-r2b-sincola | 3.290 | 12.452 | 28.320 | `384a6d5bc139cd7b…` |
| KG-Acumulado-Tandas0y1-r2b | 5.729 | 21.409 | 60.227 | `e63536d15bd8f575…` |
| KG-Acumulado-Tandas0y1-r2b-sincola | 5.729 | 20.833 | 55.358 | `0435d41f9c7b45ea…` |

| TO | unidades | con partes | aceptadas | cola | errores |
|---|---:|---:|---:|---:|---:|
| ri_gerc | 15 | 15 | 15 | 0 | 0 |
| ri_pgn | 21 | 21 | 20 | 1 | 0 |
| ceninf | 39 | 39 | 39 | 0 | 0 |
| ri_rml | 46 | 50 | 47 | 3 | 0 |
| nmcief | 55 | 55 | 55 | 0 | 0 |
| adrei | 70 | 70 | 70 | 0 | 0 |
| opefci | 74 | 74 | 74 | 0 | 0 |
| ri_dcpc | 75 | 75 | 74 | 1 | 0 |
| snp_tr | 103 | 103 | 101 | 2 | 0 |
| efemin | 119 | 119 | 116 | 3 | 0 |
| ri_mmsef | 128 | 128 | 128 | 0 | 0 |
| manori | 152 | 152 | 148 | 4 | 0 |
| expaef | 165 | 165 | 165 | 0 | 0 |
| ri_ccna | 169 | 169 | 163 | 6 | 0 |
| ayccef | 196 | 196 | 196 | 0 | 0 |
| cirmo3 | 256 | 256 | 254 | 2 | 0 |
| snp_cheq | 265 | 265 | 264 | 1 | 0 |
| cajasc | 287 | 287 | 284 | 3 | 0 |
| depaho | 442 | 442 | 436 | 6 | 0 |
| lingeef | 613 | 613 | 603 | 10 | 0 |

## 2. El costo real contra el estimado (§3, «Al cerrar»)

De `t5/salidas/costo_t5.json`. El real es el `gasto_usd` de las 40 fases de estado_corpus.json, que el runner calcula con la fórmula de caching (decisión 2 de docs/decisiones_caching_extraccion.md; data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py:328-331, e3_verificador/cliente_e3.py:194-197; precios en corpus_v2/runner_corpus.py:91-96); de cada fase se leen solo gasto_usd y resumen.n. E3 va como una sola cifra por TO, con los reintentos adentro. El estimado por TO es el del manifiesto 818a62cf… (repartido por caracteres de E0); el estimado por etapa es U × tarifa (E1 0,010135 y E3 0,010980) más las líneas de alcance en E1, repartidas por TO como en T1 (t1/t1_manifiesto.py:124-129).

| etapa | real USD | estimado con la tarifa | razón | estimado del manifiesto | razón |
|---|---:|---:|---:|---:|---:|
| E1 | 35,529339 | 33,534993 | 1,0595 | 33,575979 | 1,0582 |
| E3 (con los reintentos adentro) | 35,461693 | 36,124200 | 0,9817 | 36,083214 | 0,9828 |
| total | 70,991032 | 69,659193 | 1,0191 | 69,659193 | 1,0191 |

- **Contra el tope:** 70,991032 de 100,7291 (0,7048). `presupuesto_compartido.json` da 70,991031; la suma de las 40 fases menos ese valor, 0,000001.
- **Las líneas de alcance** en E1: USD 0,190843, repartidas por TO así: ri_gerc 0,002740, ri_pgn 0,003837, ri_rml 0,008404, nmcief 0,011109, ri_dcpc 0,013114, snp_tr 0,019558, ri_mmsef 0,023385, manori 0,026577, ri_ccna 0,028942, snp_cheq 0,053177 (en E1, por TO, `usd_agregados` de alcance_e1/a2/salidas/medicion_tanda1_a2.json (como T1)).
- **La desviación**, por etapa, por TO y total, va a: el re-presupuesto de la tanda final (docs/protocolo_entre_tandas.md:65-69).
- **La tarifa observada** (U = 3.290): E1 0,010799, E3 0,010779, juntas 0,021578, contra la de referencia 0,010135, 0,010980 y 0,021115. Es propuesta para el §5 de la tabla de reprocesamiento; T5 no la escribe en la tabla.
- **Para el pre-registro de la tanda final** (`para_el_preregistro_tanda_final`): «E1: real USD 35,5293, estimado USD 33,5350, razón 1,0595; E3: real USD 35,4617, estimado USD 36,1242, razón 0,9817; total: real USD 70,9910, estimado USD 69,6592, razón 1,0191».
- **Los pasos sin API, en 0:** E0 (T1 la generó con el código del gate, dentro del repo); la corrida en seco de T1 (clientes stub); E2 y el ensamblado de los cuatro grafos (T2 y T3); el gate, la suite, shapes, las intrínsecas y Neo4j (T3); lo contado sin leer (T3); los sorteos, el material y la lectura asistida (T4, primer tramo; lectura de la ejecutora, sin API); las tasas (T4, segundo tramo); este reporte (T5).

| TO | U | E1 real | E3 real | total real | estimado del manifiesto | razón | estimado con la tarifa | razón |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ri_gerc | 15 | 0,198871 | 0,154028 | 0,352899 | 0,408570 | 0,8637 | 0,319465 | 1,1047 |
| ri_pgn | 21 | 0,413535 | 0,382629 | 0,796164 | 0,807453 | 0,9860 | 0,447252 | 1,7801 |
| ceninf | 39 | 0,422018 | 0,386163 | 0,808181 | 1,142938 | 0,7071 | 0,823485 | 0,9814 |
| ri_rml | 46 | 1,707480 | 1,343525 | 3,051005 | 3,550498 | 0,8593 | 0,979694 | 3,1142 |
| nmcief | 55 | 1,020646 | 0,747021 | 1,767667 | 2,872825 | 0,6153 | 1,172434 | 1,5077 |
| adrei | 70 | 0,625080 | 0,651006 | 1,276086 | 1,239473 | 1,0295 | 1,478050 | 0,8634 |
| opefci | 74 | 0,609494 | 0,567516 | 1,177010 | 0,588646 | 1,9995 | 1,562510 | 0,7533 |
| ri_dcpc | 75 | 1,167431 | 0,985663 | 2,153094 | 2,154167 | 0,9995 | 1,596739 | 1,3484 |
| snp_tr | 103 | 1,200508 | 1,241520 | 2,442028 | 2,638181 | 0,9256 | 2,194403 | 1,1128 |
| efemin | 119 | 1,233886 | 1,709581 | 2,943467 | 2,527026 | 1,1648 | 2,512685 | 1,1714 |
| ri_mmsef | 128 | 0,783223 | 1,127163 | 1,910386 | 1,730887 | 1,1037 | 2,726105 | 0,7008 |
| manori | 152 | 2,292106 | 1,834569 | 4,126675 | 5,601643 | 0,7367 | 3,236057 | 1,2752 |
| expaef | 165 | 1,268476 | 1,366561 | 2,635037 | 1,437583 | 1,8330 | 3,483975 | 0,7563 |
| ri_ccna | 169 | 1,695671 | 1,823056 | 3,518727 | 3,489889 | 1,0083 | 3,597377 | 0,9781 |
| ayccef | 196 | 1,677119 | 1,955994 | 3,633113 | 2,297370 | 1,5814 | 4,138540 | 0,8779 |
| cirmo3 | 256 | 2,748674 | 2,538137 | 5,286811 | 5,157540 | 1,0251 | 5,405440 | 0,9781 |
| snp_cheq | 265 | 3,225459 | 2,838037 | 6,063496 | 7,586441 | 0,7993 | 5,648652 | 1,0734 |
| cajasc | 287 | 2,754479 | 2,979378 | 5,733857 | 4,646787 | 1,2339 | 6,060005 | 0,9462 |
| depaho | 442 | 4,003951 | 4,241745 | 8,245696 | 5,466447 | 1,5084 | 9,332830 | 0,8835 |
| lingeef | 613 | 6,481232 | 6,588401 | 13,069633 | 14,314829 | 0,9130 | 12,943495 | 1,0097 |

## 3. Los ids de modelo que devolvió la API (§2 y §5.6)

De `t5/salidas/modelos_t5.json`. Fuente: las bases de la caché del runner (data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db, e3_verificador/cache/e1_reintentos.db, e3_verificador/cache/e3_verificacion.db), ignoradas por git; copiadas con sus -wal y -shm fuera del repo, como en t2/freno_modelo_t2.py; cache.model por access_log.run_label.

| etapa | ids | respuestas distintas | esperado | igual |
|---|---|---|---|---|
| E1 | claude-haiku-4-5-20251001 | claude-haiku-4-5-20251001 3.347 | claude-haiku-4-5-20251001 | True |
| reintentos de E1 de la fase de E3 | claude-haiku-4-5-20251001 | en NO_ABRIR_conteos_t5.json: cuentan los reintentos | claude-haiku-4-5-20251001 | True |
| E3 | claude-sonnet-5 | en NO_ABRIR_conteos_t5.json: cuentan los reintentos | claude-sonnet-5 | True |

- Lo que cuenta la columna de E1: las claves distintas de la caché de E1 con las etiquetas corpus_<TO>_e1 de los 20 TOs (incluye los reintentos por corte y por forma de la fase E1).
- El manifiesto 818a62cf… no fija el id de modelo: sus sellos no tienen esa clave (solo temperaturas y namespaces).
- El freno por modelo de T2: 29 eventos en `avance_t2.jsonl`, con OK; ids de E1 claude-haiku-4-5-20251001 y de E3 claude-sonnet-5; iguales a los de las bases: True.
- Fuentes del esperado: E1, pre-registro, §2 (el freno por id); el código pide el alias claude-haiku-4-5 (runner_corpus.py:91); E3, runner_corpus.py:94 y pre-registro, §2.

## 4. Las incidencias

De `t5/salidas/incidencias_t5.json` (t2/avance_t2.jsonl (inicio_lanzador, parada, fin_lanzador) y t2/resumen_t2.json (lineas_del_runner)).

| lanzamiento de T2 | inicio | fin | pid | paradas |
|---:|---|---|---:|---|
| 1 | 2026-10-16T20:48:13-0300 | 2026-10-16T21:01:43-0300 | 76009 | 2026-10-16T21:01:43-0300: el runner salió con 3 en ri_pgn |
| 2 | 2026-10-16T23:34:21-0300 | 2026-10-17T00:17:08-0300 | 25724 | 2026-10-17T00:17:08-0300: el runner salió con 3 en ri_rml |
| 3 | 2026-10-17T08:15:22-0300 | 2026-10-17T20:52:20-0300 | 29101 | ninguna |

Los frenos por proyección del runner, tal cual: [ri_pgn] FRENO: proyección USD 104.05 supera el tope global USD 100.73 en ri_pgn:e3 21/21; [ri_rml] FRENO: proyección USD 122.79 supera el tope global USD 100.73 en ri_rml:e1 50/50.
Entre los lanzamientos: las del FRENO T2, §0 (t2/FRENO_T2.md): relanzar igual; repartir el estimado por caracteres de E0 (ca5b39fd).

Mis aclaraciones, con su ancla y sin cifras:
- **T3:** el gate pasa con las decisiones de la autora sobre su FRENO parcial (registro de decisiones, §29, puntos 1 a 7: la E0 con las partes por corte para S31; la suite sobre el acumulado, con lo «fuera del grafo» aparte; E4-a1 y E4-a4 declaradas; los `nombres_remision` de la regla v2; la fixture; las salidas de shapes y de la suite donde están; el clon declarado).
- **Las regresiones declaradas de T3:** E4-a1 y E4-a4, que se declaran y se difieren (opción (ii), registro, §29; BKL-0048). Van como hallazgos en la sección 8.
- **La regla de las dudosas** (registro de decisiones, §35): en la cola y en las dos de las aceptadas, una «dudosa» cuenta como error para la tasa, la atención y el freno; la cuenta sin ellas va al lado como sensibilidad y no decide.
- **La regla del 25 % de la cola** se disparó: la tabla 1 de la sección 5 trae su cifra. La investigación de su causa la diseña la mesa (sección 9).

## 5. Las tasas de T4

La tabla 1 de `t4/tablas_t4_tramo2.md`, que genera `t4/scripts/tablas_t4t2.py` desde `t4/tasas/tasas_t4_tramo2.json` (sha256 `ac6e48a238226833053387cdcd7cf70397db18cdacefc22c92ee99557ff826a2`), tal cual. Sus rutas son relativas a `data/experiment/tanda1/t4/`.

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda 1 | línea de base | decisión | script y clave de la salida |
|---|---|---|---|---|
| aceptadas, ítems | 9 de 30 (5 con error y 4 dudosas); ponderada 0,2196, Wilson [0,0784; 0,4822] (n ef. 13,912); sin las dudosas, 5 de 26, 0,1209 [0,0285; 0,3916] | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,3618); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.items` |
| aceptadas, no ítems | 3 de 30 (2 con error y 1 dudosa); ponderada 0,0968, Wilson [0,0214; 0,3446] (n ef. 14,130); sin las dudosas, 2 de 29, 0,0907 [0,0192; 0,3374] | 4 de 30, Wilson [0,0531; 0,2968] | atención: no (p 0,6454); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.no_items` |
| aceptadas, ponderada total | 0,1397, Wilson [0,0532; 0,3196] (n ef. 25,817); sin las dudosas, 0,1013 [0,0322; 0,2759] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.total` |
| atención de RI | 7 de 30; ponderada de RI 0,1747, Wilson [0,0715; 0,3680] (n ef. 23,906); sin las dudosas, 3 de 26, 0,0842 | bajo H0, 0,1572 (umbral de T3: 0,2913) | atención: no (p 0,3510) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `atencion_RI` |
| tasa de error de la cola | 14 de 30 (12 con error y 2 dudosas); ponderada 0,4386, Wilson [0,2751; 0,6166] (n ef. 28,646); sin las dudosas, 12 de 28, 0,3984 [0,2376; 0,5847] | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `cola` |
| observación (12) | 27 correctas de 30 (0 no decidibles, en el denominador; 3 incorrectas: E1-prompt 3); Wilson [0,7438; 0,9654]; ponderada por celda 0,8916 [0,6467; 0,9737] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro, §5.2) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `observacion:12` |
| vigilancia (1) | 3 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,1000, Wilson [0,0346; 0,2562]; ponderada por celda 0,1043 [0,0242; 0,3532] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 15 vaciamientos de 30; cruda 0,5000, Wilson [0,3315; 0,6685]; ponderada por celda 0,5276 [0,3354; 0,7120] | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 9 duplicaciones de 30; cruda 0,3000, Wilson [0,1666; 0,4788]; ponderada por celda 0,3199 [0,1665; 0,5255] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 4; cruda 0,5000, Wilson [0,1500; 0,8500]; leída entera, sin celdas | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, no; la de RI, no. Hay ampliación: no. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items no, RI no.
- **Los controles de la entrada** (`scripts/tasas_t4t2.py`): 37 de 37 pasan.

## 6. La columna «Tanda 1» del tablero de correcciones (§5.2)

De `t5/salidas/columna_tanda1_t5.json`: las celdas de T3, tal cual, y la que esperaba a T4 (la fila 59). La misma tabla va como propuesta aparte en `t5/columna_tanda1_tablero_PROPUESTA.md`; el tablero del repo no se toca.

| fila | síntoma | Tanda 1 | ancla |
|---:|---|---|---|
| 49 | **Observación (10):** extracción más magra | veinte 5,74 (18.887 / 3.290); veinte sin cola 5,62 (18.483 / 3.290); acumulado 5,61 (32.138 / 5.729); acumulado sin cola 5,47 (31.348 / 5.729). Base re-sellada: diez 5,43 (13.251 / 2.439) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 50 | **Observación (11):** menos remisiones entre documentos | veinte 1.541 `remite_a` entre documentos (1.272 menciones); veinte sin cola 299 `remite_a` entre documentos (1.224 menciones); acumulado 3.628 `remite_a` entre documentos (2.783 menciones); acumulado sin cola 2.061 `remite_a` entre documentos (2.698 menciones). Base re-sellada: diez 642; desarrollo 497 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 51 | **Aristas `referencia` por tipo de origen:** ninguna sale de Condicion, Potestad ni Definicion | veinte 3.080 remisiones desde Condicion, Definicion o Potestad; 0 `referencia` con origen distinto de TextoOrdenado; veinte sin cola 2.207 remisiones desde Condicion, Definicion o Potestad; 0 `referencia` con origen distinto de TextoOrdenado; acumulado 8.449 remisiones desde Condicion, Definicion o Potestad; 0 `referencia` con origen distinto de TextoOrdenado; acumulado sin cola 7.055 remisiones desde Condicion, Definicion o Potestad; 0 `referencia` con origen distinto de TextoOrdenado | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 52 | **Condiciones sin regla** (antes «Condiciones aisladas»; redefinida por decisión de la autora del 07/10/2026) | veinte 222 sin regla de 1.425 Condicion; aislados 16; veinte sin cola 221 sin regla de 1.401 Condicion; aislados 16; acumulado 550 sin regla de 3.367 Condicion; aislados 23; acumulado sin cola 541 sin regla de 3.266 Condicion; aislados 23 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 53 | **Remisiones falsas por paráfrasis** | veinte no aplica: el grafo no tiene cap; veinte sin cola no aplica: el grafo no tiene cap; acumulado 0 hacia cap 6.5.1 o debajo, de 28 remisiones desde cap::8.2.3.3; acumulado sin cola 0 hacia cap 6.5.1 o debajo, de 28 remisiones desde cap::8.2.3.3 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 54 | **Test del ejemplo `cla::5.1.1.1`** | veinte no_aplicable (fuera del grafo: no cuenta, decisión 3); veinte sin cola no_aplicable (fuera del grafo: no cuenta, decisión 3); acumulado resuelto; acumulado sin cola resuelto | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 55 | **Regresiones de la suite contra r1** | veinte 31 / 16 / 21, contra r1 de resuelto a persiste 8; no declaradas que cuentan en el gate: 0; veinte sin cola 31 / 16 / 21, contra r1 de resuelto a persiste 8; no declaradas que cuentan en el gate: 0; acumulado 46 / 13 / 9, contra r1 de resuelto a persiste 5; no declaradas que cuentan en el gate: 0; acumulado sin cola 46 / 13 / 9, contra r1 de resuelto a persiste 5; no declaradas que cuentan en el gate: 0 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 56 | **Patrón de navegación (a):** ancla vista por `referencia` sin abrir | no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 57 | **Patrón de navegación (b):** vecinos solo salientes sobre una Operacion con restricciones entrantes | no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 58 | **Tope de herramientas alcanzado** | no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 59 | **Incorrectas de la observación (12), por capa** | veinte sin cola (el evaluado; lectura de T4): 27 correctas de 30, Wilson [0,7438; 0,9654]; 0 no decidibles; incorrectas por capa: E1-prompt 3. Ponderada por celda 0,8916. Base: 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro, §5.2) | t4/tasas/tasas_t4_tramo2.json, observacion:12 (scripts/tasas_t4t2.py) |
| 60 | **Clases de falla A0.2** | no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 61 | **Unidades cortadas o mudas** | veinte 0 de 3.294 (E0 con las partes); veinte sin cola 42 de 3.294 (E0 con las partes); acumulado 0 de 5.734 (E0 con las partes); acumulado sin cola 111 de 5.734 (E0 con las partes) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 62 | **Afirmación falsa por tabla no detectada (`cap::1.2`, `BKL-0006`)** | veinte no aplica: el grafo no tiene cap; BKL-0006 no_aplicable, BKL-0023 no_aplicable; veinte sin cola no aplica: el grafo no tiene cap; BKL-0006 no_aplicable, BKL-0023 no_aplicable; acumulado 1 umbral(es) 5000000000 moneda ARS; 1 umbral(es) 2500000000 moneda ARS; BKL-0006 resuelto, BKL-0023 resuelto; acumulado sin cola 1 umbral(es) 5000000000 moneda ARS; 1 umbral(es) 2500000000 moneda ARS; BKL-0006 resuelto, BKL-0023 resuelto | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 63 | **Pérdidas de contenido por tablas** | veinte no aplica: el grafo no tiene los TOs de las citas de D2 ni de las unidades de U-UMBRAL; veinte sin cola no aplica: el grafo no tiene los TOs de las citas de D2 ni de las unidades de U-UMBRAL; acumulado 5 de 5 citas presentes (R-PRES); acumulado sin cola 5 de 5 citas presentes (R-PRES) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 64 | **Valores fuera de lista cerrada** | veinte Restriccion.tipo 0, Comunicacion.tipo 32, Obligacion.tipo 0, Obligacion.frecuencia 218; claves fuera 0; veinte sin cola Restriccion.tipo 0, Comunicacion.tipo 32, Obligacion.tipo 0, Obligacion.frecuencia 214; claves fuera 0; acumulado Restriccion.tipo 0, Comunicacion.tipo 58, Obligacion.tipo 0, Obligacion.frecuencia 282; claves fuera 0; acumulado sin cola Restriccion.tipo 0, Comunicacion.tipo 57, Obligacion.tipo 0, Obligacion.frecuencia 277; claves fuera 0. `properties_no_definidas`: en NO_ABRIR_conteos_t3.json (cuenta `copia_nota_e3`, bajo el cegamiento, y la marca de L-04) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 65 | **Mención del sujeto sin guardar; sujetos no mapeables** | veinte 4.469 de 4.469 con mención; propuestos en el grafo 284; veinte sin cola 4.374 de 4.374 con mención; propuestos en el grafo 280; acumulado 7.078 de 7.078 con mención; propuestos en el grafo 379; acumulado sin cola 6.912 de 6.912 con mención; propuestos en el grafo 373 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 66 | **Catálogo de sujetos en dos fuentes** | 0 / 0 (ids solo en el bloque / solo en el catálogo; 110 en el bloque) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 67 | **Cuantías sin campo estructurado** | veinte 6 sin campo de 685 con cuantía; veinte sin cola 6 sin campo de 663 con cuantía; acumulado 10 sin campo de 1.469 con cuantía; acumulado sin cola 10 sin campo de 1.421 con cuantía | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 68 | **Omisiones sin registro fuera de los chunks marcados** | veinte 2.055 unidades con omisiones; sin categoría 2, sin tramo 5; registro del ensamblado 2.610 filas; veinte sin cola 2.055 unidades con omisiones; sin categoría 2, sin tramo 5; registro del ensamblado 2.533 filas; acumulado 3.705 unidades con omisiones; sin categoría 2, sin tramo 6; registro del ensamblado 4.491 filas; acumulado sin cola 3.705 unidades con omisiones; sin categoría 2, sin tramo 6; registro del ensamblado 4.340 filas | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 69 | **Crudo del reintento de E3 sin persistir** | en NO_ABRIR_conteos_t3.json: usa los reintentos de E3 (cegamiento de U-MED-VERIF, punto 8) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 70 | **Colisiones de ids de chunk en E0 (`BKL-0037`)** | veinte 0 ids repetidos; veinte sin cola 0 ids repetidos; acumulado 0 ids repetidos; acumulado sin cola 0 ids repetidos | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 71 | **Relaciones de la matriz ampliada sin verificar por E3** (`condicion_de` → Operacion y → Potestad) | veinte 0; veinte sin cola 0; acumulado 0; acumulado sin cola 0 | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 72 | **Líneas en mayúsculas descartadas al tope de la página (E0 legada)** | no medido: la fila lee r1k_encabezados_descartados_e0r2.json, medido sobre la E0 legada de la tanda 0; la tanda 1 no tiene E0 legada | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 73 | **Pies de página dentro del texto de E0** | veinte 0 de 3.290 chunks (0 líneas); veinte sin cola 0 de 3.290 chunks (0 líneas); acumulado 0 de 5.729 chunks (0 líneas); acumulado sin cola 0 de 5.729 chunks (0 líneas) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |
| 74 | **Plazos sin cuantía mandados a `frecuencia`** | veinte 0 a `frecuencia`, 0 fuera de la lista (control con el reporte: True); veinte sin cola 0 a `frecuencia`, 0 fuera de la lista (control con el reporte: True); acumulado 0 a `frecuencia`, 0 fuera de la lista (control con el reporte: True); acumulado sin cola 0 a `frecuencia`, 0 fuera de la lista (control con el reporte: True) | t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py) |

## 7. El alcance y el catálogo al cierre (§5.5)

De `t5/salidas/alcance_catalogo_t5.json`, desde `t3/conteos_sin_leer/contado_sin_leer_t3f.json`.

| registro | filas | en cuarentena | verificadas en cuarentena | claves | con 2 unidades o más | con 3 o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|---:|---:|
| veinte | 908 | 703 | 570 | 237 | 38 | 12 | 8 |
| veinte_sincola | 896 | 693 | 561 | 233 | 37 | 12 | 8 |
| acumulado | 1.186 | 851 | 713 | 320 | 56 | 19 | 13 |
| acumulado_sincola | 1.169 | 839 | 702 | 315 | 54 | 19 | 12 |

- **El umbral:** 2 unidades distintas (enmienda 4, §1, punto 2, y decisión 1 al firmar). Las claves: solo cuántas: son menciones de unidades que no están todas en unidades_a_la_vista_T4.json; la lista está en t3/conteos_sin_leer/contado_sin_leer_t3f.json (catalogo_al_cierre), commiteada.
- **Desvío del §5.5, declarado:** el catálogo no crece en la tanda 1; la lectura de sus claves se hace una sola vez, sobre el acumulado de las tres tandas (pre-registro de la tanda final, versión para firmar v3, §9, decisión 4); se declara como desvío del §5.5 del pre-registro de la tanda 1.
- **Cuántas relaciones resolvió cada versión del catálogo:** hubo 1, la de la release (catálogo del request c3ad1581…, sin ampliaciones del catálogo de resolución). En el evaluado, E1 dio 3.950 relaciones con `sujeto_id` y 434 con `sujeto_propuesto`; el registro de no mapeados tiene 896 filas (cuarentena 693, resuelto_a_clase 201, descartado 2). Fuente: t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola (vigilancias.8 y f65_sujetos.registro_no_mapeados). La cuenta por versión de la enmienda 4 (§1, punto 5) sigue a una re-resolución, que en la tanda 1 no corre.
- **El ensamblado de la tanda 1 corrió sin catálogo de resolución:** True (ningún script de `t3/scripts/` lo nombra).
- **El alcance que leyó E1:** `data/experiment/catalogo_unico/registro_alcance_r2b.json`, `e06933e77a1ae819…`, igual al sello del manifiesto: True. Las líneas de alcance: 1.029 unidades, 190.841 tokens, USD 0,190841.

## 8. Los hallazgos, en los ejes A y B (§5.6; protocolo entre tandas, `:71-100`)

De `t5/salidas/hallazgos_t5.json`. Cuántos: incorrecta de una lectura de T4, 10; la cola, con la regla del 25 % disparada, 1; regresión declarada de T3, 2; vigilancia fuera de su línea de base, 3; fila del tablero que no cumple su meta, 3. Propuestas del backlog: 11, en `t5/propuestas_backlog_t5.jsonl` (no se escriben en el backlog).

| id | tipo | qué | cifra o veredicto | capa_pipeline | eje A | eje B | backlog |
|---|---|---|---|---|---|---|---|
| H01 | incorrecta de una lectura de T4 | aceptadas, ítems: `ri_ccna::D1F2::3.5` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H02 | incorrecta de una lectura de T4 | aceptadas, ítems: `ri_dcpc::3.4.4.1` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H03 | incorrecta de una lectura de T4 | aceptadas, ítems: `nmcief::A6::Sbloque12` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H04 | incorrecta de una lectura de T4 | aceptadas, ítems: `nmcief::A6::Sbloque8` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H05 | incorrecta de una lectura de T4 | aceptadas, ítems: `lingeef::3.1.2.2` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H06 | incorrecta de una lectura de T4 | aceptadas, no ítems: `ri_ccna::D1A3L2::S7` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H07 | incorrecta de una lectura de T4 | aceptadas, no ítems: `depaho::3.15::intro` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H08 | incorrecta de una lectura de T4 | observación (12): `ri_rml::Sbloque11` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H09 | incorrecta de una lectura de T4 | observación (12): `nmcief::A3::S2` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H10 | incorrecta de una lectura de T4 | observación (12): `efemin::7.7` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H11 | la cola, con la regla del 25 % disparada | `cola` | 14 de 30; ponderada 0,4386, Wilson [0,2751; 0,6166]; sin las dudosas, 12 de 28 | no dicha por la lectura | sin fila: la regla, si se dispara, re-procesa las unidades de la cola o las saca del grafo evaluado (enmienda de la cola humana, §1, punto 6); el evaluado ya es el sin cola | la investigación de su causa, antes de la tanda final y sin cambiar el grafo sin cola (pre-registro, 95b18217:634-635); la diseña la mesa, no es de T5 | no: queda para la investigación de la causa |
| H12 | regresión declarada de T3 | `E4-a1` | persiste | E1-prompt (la de BKL-0048) | F06 todo: por la capa de BKL-0048, E1-prompt | se difiere: decisión de la autora del 18/10/2026, opción (ii) (registro de decisiones, §29) | ya está: BKL-0048 |
| H13 | regresión declarada de T3 | `E4-a4` | persiste | E1-prompt (la de BKL-0048) | F06 todo: por la capa de BKL-0048, E1-prompt | se difiere: decisión de la autora del 18/10/2026, opción (ii) (registro de decisiones, §29) | ya está: BKL-0048 |
| H14 | vigilancia fuera de su línea de base | `(5)` | requisito_de_estructura 0, tipo_obligacion_normalizados 1 | no dicha: es un conteo, sin lectura | nada: requisito_de_estructura da 0, como su línea de base; el contador de normalizados da 1 contra 0: el validador ya normalizó el valor, y se declara como residuo | no se corrige: residuo declarado | no |
| H15 | vigilancia fuera de su línea de base | `(8)` | sujeto_propuesto 434 de sujeto_id 3950 (9,90 %) | catálogo (la del remedio previsto: el crecimiento del catálogo de resolución, enmienda 4) | F13 solo código sobre lo guardado: el catálogo de resolución crece al cierre y actúa sobre la mención guardada | se corrige antes del sello del grafo evaluado, con la lectura única de las claves sobre las tres tandas (pre-registro de la tanda final, v3, §9, decisión 4), si la autora la aprueba a tiempo | no: va por la lectura de las claves |
| H16 | vigilancia fuera de su línea de base | `(9)` | 7 emisiones en E1 (snp_tr 7); 20 aristas en el grafo | no dicha: es un conteo, sin lectura | sin fila: hace falta leer las emisiones (el instrumento de la vigilancia es un muestreo) | se difiere: la lectura de las emisiones no está despachada | propuesta |
| H17 | fila del tablero que no cumple su meta | `fila 64` | Comunicacion.tipo sin marca ni original 32: el residuo que la meta declara (Comunicacion sin `tipo`; L-04) | no dicha: es un conteo, sin lectura | F14b solo código sobre lo guardado: si la lectura de L-04 llega al piso, la corrige su código previsto (la marca tipo_no_derivable de validador_r2; §6.7) | se corrige entre tandas solo por la regla de L-04 (§6.7), que no está despachada (registro de decisiones, §29); si no llega al piso, queda el residuo declarado | no |
| H18 | fila del tablero que no cumple su meta | `fila 67` | 6 sin campo de 663 con cuantía: el residuo que la meta declara (4 en diez) | no dicha: es un conteo, sin lectura | nada: se declara como residuo, como en la tanda 0 (tablero:67) | no se corrige: residuo declarado | no |
| H19 | fila del tablero que no cumple su meta | `fila 68` | sin categoría 2, sin tramo 5: el residuo que la meta declara (1 sin tramo por grafo) | no dicha: es un conteo, sin lectura | nada: se declara como residuo, como en la tanda 0 (tablero:68) | no se corrige: residuo declarado | no |

**La causa de cada hallazgo**, tal cual (la de las lecturas es la nota de la autora; sin nota, «causa: no dicha por la lectura»):

- **H01** (`ri_ccna::D1F2::3.5`): causa: no dicha por la lectura
- **H02** (`ri_dcpc::3.4.4.1`): causa: no dicha por la lectura
- **H03** (`nmcief::A6::Sbloque12`): causa: no dicha por la lectura
- **H04** (`nmcief::A6::Sbloque8`): causa: no dicha por la lectura
- **H05** (`lingeef::3.1.2.2`): causa: no dicha por la lectura
- **H06** (`ri_ccna::D1A3L2::S7`): N1 (la valuación debe seguir las normas del BCRA) es el criterio que la revisión controla, no un supuesto de ella; condicion_de hacia N3 lo invierte, como en items 17 y 19
- **H07** (`depaho::3.15::intro`): aplica_a al rol de todas las entidades intervinientes, pero el texto obliga solo a las del Grupo A (regla de cola 10)
- **H08** (`ri_rml::Sbloque11`): el 9.1.4 resta del control de la partida 210100 los saldos del 210105, que son justamente los bonos depositados en la CRyL y aplicados al incremento de exigencia; esos bonos quedan fuera del límite, así que la arista invierte el efecto (el tope sobre su aplicación es otro: 210105 ≤ 824000/001, en la tabla). La firma es válida, el error es de lectura del modelo
- **H09** (`nmcief::A3::S2`): el chapeau presenta la verificación como procedimiento que debe cumplir el auditor interno («independientemente del análisis de riesgos que efectúe el auditor interno, se deberán cumplimentar…»); en el texto la entidad aparece como auditada, no como quien verifica, y el modelo tomó esa mención como sujeto del deber (R-a: el texto nombra otro sujeto)
- **H10** (`efemin::7.7`): el 7.7 no prohíbe otorgar esas financiaciones, que son justamente las que reducen la exigencia; prohíbe computarlas además en las deducciones de otros puntos; la descripción del origen es fiel, pero la arista afirma que la financiación está prohibida (como cola 18, destino equivocado de la restricción); firma válida, error de lectura del modelo
- **H11** (`cola`): por unidad, en `unidades`: la nota de la autora, o «causa: no dicha por la lectura»; la causa de que se dispare la regla es la que investiga la mesa
  - `ri_ccna::D1F2::3.7` (RI:sin_raiz, dudosa): causa: no dicha por la lectura
  - `ri_ccna::D1F2::S1` (RI:sin_raiz, con error): causa: no dicha por la lectura
  - `ri_ccna::D2A2::S1` (RI:sin_raiz, con error): causa: no dicha por la lectura
  - `ri_dcpc::3.1.1` (RI:resto, con error): causa: no dicha por la lectura
  - `ri_rml::Sbloque10` (RI:resto, con error): causa: no dicha por la lectura
  - `ri_rml::Sbloque14::parte1` (RI:resto, con error): e4 aplica_a al rol de todas las entidades comprendidas, pero el punto 11.1 rige solo para las de Grupo A y el texto da otra regla a las B y C
  - `ri_rml::Sbloque14::parte4` (RI:resto, con error): e9 convierte en tope de las financiaciones la TNA del 24 %, que el texto usa solo para definir cuáles computan en la partida 712000/001
  - `lingeef::3.5.4.3` (NG:resto, con error): causa: no dicha por la lectura
  - `lingeef::5.4.2.3` (NG:resto, con error): causa: no dicha por la lectura
  - `depaho::3.8.3.4` (NG:resto, con error): causa: no dicha por la lectura
  - `efemin::6.4.3.1` (NG:resto, con error): causa: no dicha por la lectura
  - `lingeef::11.1.2` (NG:resto, con error): causa: no dicha por la lectura
  - `cajasc::3.7.3` (NG:resto, dudosa): causa: no dicha por la lectura
  - `depaho::4.19.4` (NG:resto, con error): causa: no dicha por la lectura
- **H12** (`E4-a1`): la de BKL-0048: la relación aplica_a de su unidad trae una mención que no está en el texto de la unidad, no verifica y va a cuarentena; la suite lo cuenta porque mira la etiqueta con la regla de E4 de r1 (data/backlog/backlog.jsonl, BKL-0048)
- **H13** (`E4-a4`): la de BKL-0048: la relación aplica_a de su unidad trae una mención que no está en el texto de la unidad, no verifica y va a cuarentena; la suite lo cuenta porque mira la etiqueta con la regla de E4 de r1 (data/backlog/backlog.jsonl, BKL-0048)
- **H14** (`(5)`): no dicha: es un conteo, sin lectura
- **H15** (`(8)`): no dicha: es un conteo, sin lectura
- **H16** (`(9)`): no dicha: es un conteo, sin lectura. La vigilancia pregunta por las emisiones fuera del dominio de pagos; si las de snp_tr lo están no lo leí: NO VERIFICADO
- **H17** (`fila 64`): no dicha: es un conteo de T3, sin lectura
- **H18** (`fila 67`): no dicha: es un conteo de T3, sin lectura
- **H19** (`fila 68`): no dicha: es un conteo de T3, sin lectura

**Las dudosas de las aceptadas, aparte** (5): la lectura no las decidió: cuentan como error para la tasa, la atención y el freno (regla de las dudosas), y no van como hallazgo ni al backlog; quedan para la mesa.

- `ri_mmsef::2.2.10.2` (aceptadas, ítems, RI:sin_raiz; propuesta dudosa): causa: no dicha por la lectura
- `ri_mmsef::2.2.13.1` (aceptadas, ítems, RI:sin_raiz; propuesta dudosa): causa: no dicha por la lectura
- `ri_dcpc::3.2.2.1` (aceptadas, ítems, RI:resto; propuesta dudosa): causa: no dicha por la lectura
- `expaef::9.6.4` (aceptadas, ítems, NG:resto; propuesta dudosa): causa: no dicha por la lectura
- `ri_ccna::D1A3L2::S33` (aceptadas, no ítems, RI:sin_raiz; propuesta con error): aplica_a a las cajas de crédito sigue el alcance del TO, pero es una prueba sustantiva sobre «la entidad», que apunta al auditor externo; el texto no nombra al obligado

**Lo que no es hallazgo por estas reglas:**
- las vigilancias (1), (2), (3) y (7): (1) sí 3, no 27, no decidible 0; (2) vaciamiento 15, no vaciamiento 15, no decidible 0; (3) duplicación 9, distintos 21; (7) con apoyo 2, sin apoyo 2, no decidible 0 (la tanda 0 no las leyó (pre-registro, §5.3): no hay una línea de base que pasar);
- la vigilancia (4): un TextoOrdenado por TO, True; las aceptadas: sin atención ni freno (tasas_t4_tramo2.json);
- las filas del tablero, por la lectura de su meta (mía, en `REGLA_FILAS` de `cifras_t5.py`): 49 sin meta numérica; 50 no medida; 51 no aplica; 52 no medida; 53 cumple; 54 cumple; 55 cumple; 56 residuo declarado; 57 residuo declarado; 58 residuo declarado; 59 hallazgos por la lectura; 60 residuo declarado; 61 cumple; 62 cumple; 63 cumple; 65 cumple; 66 cumple; 69 no medida; 70 cumple; 71 cumple; 72 no aplica; 73 cumple; 74 cumple.

## 9. Lo que sigue, sin hacerlo en T5

1. **La investigación de la causa de la cola,** antes de la tanda final y sin cambiar el grafo sin cola (pre-registro, `95b18217:634-635`). La diseña la mesa.
2. **La vigilancia (3),** con 9 duplicaciones de 30, y la unión de nodos que esperaba a su resultado (registro de decisiones, §32: «Unir nodos con los de la unidad de origen espera a lo que encuentre la (3). Sacarlos, no.»).
3. **La vigilancia (2),** con 15 vaciamientos de 30, y la (7), con 2 sin apoyo de 4.
4. **El conteo de `cid`** (pre-registro, §6.9) y **las FICHAS** de U-MED-VERIF, que van después del commit de T5.

## 10. Las fuentes que leyó `cifras_t5.py`

De `t5/salidas/fuentes_t5.json`, con el sha256 de cada una en la copia.

| archivo | sha256 |
|---|---|
| `data/experiment/alcance_e1/a2/salidas/medicion_tanda1_a2.json` | `1cbe7df08e409f2c1fd560abff264bf773c36dafe9897acdd9b4df37d181416b` |
| `data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/estado_corpus.json` | `6b958b63f539b84e219f0857025e2ae5278835d7238a9dea510cfb68b8d1758d` |
| `data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b/presupuesto_compartido.json` | `ecccbf2b1de537150d0844368c796216a63dc2f64ef0c6574f13b3ccde385e55` |
| `data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json` | `818a62cfde403a453d0551916022f928f7cd9cb62d7947801eadb587f2385d9d` |
| `data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json` | `22f33a175697304da213453f9a8ab11dcbbd210b75adcddf3741f66a81be2f5a` |
| `data/experiment/tanda1/t2/avance_t2.jsonl` | `0be260e5e36aa6ecb077661950d0de96e07780fd375c9de02fca2ed8b6767a48` |
| `data/experiment/tanda1/t2/resumen_t2.json` | `b4453e5fc5526b906ace503da4dbcaef91006379c6b1fbb13bbdd87adf7e4e71` |
| `data/experiment/tanda1/t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md` | `3867a630c12a2a879e059359ebd4d2c70358cff6193450419baf460fa9bf4d7c` |
| `data/experiment/tanda1/t3/conteos_sin_leer/contado_sin_leer_t3f.json` | `226a404154c2458e5c750c8cb59cdc458dbe3880f4cf9c1282d5cb9f6a5a4944` |
| `data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json` | `5ec9753dc9f8caa51a37a884c542efe38416a41d575a030b24ababbf9c60b17d` |
| `data/experiment/tanda1/t3/salidas/clasificacion_regresiones_t3.json` | `be2ad31cb11a7829ef5f96a3bbaebbc56e5e0003045af05fad237067f92012de` |
| `data/experiment/tanda1/t3/salidas/doble_corrida_t3.json` | `8d8649461ecdebc33fd040e91f15ae5e6802f2fe24547f783c8bc6735be1d854` |
| `data/experiment/tanda1/t4/lectura_autora/aceptadas_items_marcada.csv` | `88526906a7443187192dc2cc50eacc82635ccf2b744cc075ffe3d6fa0851a723` |
| `data/experiment/tanda1/t4/lectura_autora/aceptadas_no_items_marcada.csv` | `dda313dc6add4592c66a6ea64ca4807403ef7f144658677850d46548cc275eb5` |
| `data/experiment/tanda1/t4/lectura_autora/cola_marcada.csv` | `818850df2cb0a68018fcc23dbf886f1d8695e4b91e063668f156b949f5baafdb` |
| `data/experiment/tanda1/t4/lectura_autora/observacion_12_marcada.csv` | `b1ffe65c7390c763b9f05890a198d58aa3346638f47964551cd03333187caa94` |
| `data/experiment/tanda1/t4/muestras/material/observacion_12/fichas_observacion_12.jsonl` | `8528dce6ab8c5e27ed5560336b38d983cdfc77ceb51831cc939c0588fc8bff64` |
| `data/experiment/tanda1/t4/tasas/tasas_t4_tramo2.json` | `ac6e48a238226833053387cdcd7cf70397db18cdacefc22c92ee99557ff826a2` |
| `docs/tablero_correcciones.md` | `5b2840b97f5eec0f94a59a84848a4793102b98743cbbb26f99ab829c9b702498` |

## 11. El selftest de claves

De `t5/salidas/selftest_t5.json`: veredicto general OK; A, anclaje del perfil sellado (v3_b54), E1: OK; A, anclaje del perfil sellado (v3_b54), E3: OK; B, variaciones del perfil sellado: OK; inventario del armado del perfil sellado: OK; A', anclaje del perfil r2b, E1: OK; A', anclaje del perfil r2b, E3: OK; B', variaciones del perfil r2b: OK; inventario del armado del perfil r2b: OK; C, contraste con la tabla de reprocesamiento: OK. Las dos corridas, iguales: True. Es el selftest de la tanda 0, tal cual: controla que la tanda 1 no tocó sus claves; para la tanda 1 no se adaptó. Los conteos, en `t5/NO_ABRIR_conteos_t5.json`.
