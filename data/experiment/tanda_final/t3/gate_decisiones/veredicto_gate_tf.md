#### Tabla V0. La E0 con las partes por corte (`gate_decisiones/e0_partes_tf.json`)

| E0 | archivos | dos corridas iguales | unidades reemplazadas por sus partes | sha256 del conjunto |
|---|---:|---|---:|---|
| tanda_final | 498 | True | 0 | `fa6cc1c0dfc2517135ddf5fd693a04a3eb5cbd400f6e6304c443f80f945f6bb1` |
| acum128 | 640 | True | 2 | `8c2471dd2b486e4505646acb7898889006ebafb1ad9a45bd891352325a111567` |
| acum60 | 300 | True | 2 | `4b0831fc022799a4d3ddba4e4d492bbf0be238af46fb582e321daef74d9053d7` |

Controles: la de la tanda final es la E0 del repo: True; en los acumulados, los archivos de las tandas 0 y 1 son los de la E0 con las partes del acumulado de la tanda 1 y los de la tanda final, los de la suya: acum128 150 y 490 archivos, True; acum60 150 y 150 archivos, True.

#### Tabla V1. El veredicto del gate por grafo

| grafo | shapes, E0 con las partes (rige) | shapes, E0 del grafo (informada) | suite: resuelto / persiste / no aplica | regresiones | declaradas (laudo) | declaradas (§29) | fuera del grafo | no declaradas que cuentan |
|---|---|---|---|---:|---:|---:|---:|---|
| KG-TandaFinal-r2b | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-r2b-sincola | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-Tramo1-r2b | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-TandaFinal-Tramo1-r2b-sincola | PASA (22 / 2 / 4) | PASA (22 / 2 / 4) | 33 / 14 / 21 | 18 | 3 | 0 | 18 | 0 |
| KG-Acumulado-Tandas0y1yFinal-r2b | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |

Las columnas de shapes dan PASS / FAIL / WARN; los FAIL que no bloquean, por grafo, están en `tablas_gate_tf.json` (`no_pass`). «Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo no tiene; en los acumulados no se aplica (§29). La entrada de la fixture contra la que se mide cada grafo es la suya (las ocho nuevas heredan las expectativas de la tanda 1).
- **KG-TandaFinal-r2b, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 29 fuera del grafo, 38 generales y 1 en el grafo. Cruce con acum128: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-r2b-sincola, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 29 fuera del grafo, 38 generales y 1 en el grafo. Cruce con acum128_sincola: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-Tramo1-r2b, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con acum60: 15 y 15 ítems, iguales: True.
- **KG-TandaFinal-Tramo1-r2b-sincola, «fuera del grafo»:** 18 regresiones; de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con acum60_sincola: 15 y 15 ítems, iguales: True.

#### Tabla V2. S31 con la E0 de cada grafo: la causa, por id (`gate_decisiones/causa_s31_tf.json`)

| grafo | `remite_a` | con su chunk fuera de la E0 del grafo | todos son partes por corte |
|---|---:|---:|---|
| KG-TandaFinal-r2b | 19076 | 0 | True |
| KG-TandaFinal-r2b-sincola | 16889 | 0 | True |
| KG-TandaFinal-Tramo1-r2b | 750 | 0 | True |
| KG-TandaFinal-Tramo1-r2b-sincola | 737 | 0 | True |
| KG-Acumulado-Tandas0y1yFinal-r2b | 53885 | 3528 | True |
| KG-Acumulado-Tandas0y1yFinal-r2b-sincola | 44821 | 997 | True |
| KG-Acumulado-Tandas0y1yTramo1-r2b | 29847 | 3435 | True |
| KG-Acumulado-Tandas0y1yTramo1-r2b-sincola | 23314 | 997 | True |

#### Tabla V3. La doble corrida, la reproducibilidad, la fixture, los selftests y lo informativo

- **La doble corrida** de los ocho: True; **la reproducibilidad**: 10 cadenas, todas iguales a su sello: True; veredicto OK (`salidas/doble_corrida_tf.json`).
- **La fixture** (`gate_decisiones/control_fixture_tf.json`): 4094 claves de HEAD, 0 quitadas y 0 cambiadas; 2272 claves nuevas, todas de las ocho entradas nuevas: True; veredicto OK.
- **Los selftests:** catalogo_unico rc=0, e0 rc=0, ensamblado_omisiones rc=0, metrica_condiciones rc=0, pyd_r2 rc=0, r3 rc=0, regression_kg_1 rc=0, regression_kg_2 rc=0, shapes_congelado rc=0. **El de claves**, sin las cuentas: no se lee: el JSON va a un NO_ABRIR_; sus dos salidas sin cuentas, byte a byte las de A3: False y False.
  - **La causa del de claves** (`gate_decisiones/diagnostico_clave_cache_tf.json`, sin abrir sus salidas): los 16 campos que difieren de A3 sin cuentas son de la variación del TO nuevo (`variacion_to_nuevo`, R23 en el perfil r2b) o derivan de ella: True. Supone que `snp_psp::1.3.1.1` no está en la caché de E1; `snp_psp` es de la tanda final (82.º de `orden_corrida`, tramo 2) y su chunk es el mismo en la E0 de la tanda final y en b584: True. La fila del contraste que difiere, filas[32]/observado[0]: F17 (R23), es la de R23: True. R23 supone que la unidad de un TO fuera de la tanda 0 no está en la caché de E1. T2 extrajo ese TO con el perfil r2b y el mismo chunk, así que la clave está y R23 deja de dar miss: el selftest falla por su supuesto, no por el código de la clave.
  - **Declaradas no aplicables después de T2** (decisión de la autora sobre el FRENO T3 parcial): la R23 del perfil r2b y la V23 del sellado. Sin ellas, todo lo demás del selftest es igual a A3 sin cuentas: True. El selftest no se tocó; el cambio de su TO lo hace la mesa aparte.
- **Las intrínsecas de generación 3, con la E0 con las partes (informativas):**
  - KG-TandaFinal-r2b: M4 5.435888, M9 34 nodos aislados, M10 1 / 4951.
  - KG-TandaFinal-r2b-sincola: M4 5.228582, M9 31 nodos aislados, M10 81 / 4951.
  - KG-TandaFinal-Tramo1-r2b: M4 3.428331, M9 13 nodos aislados, M10 1 / 601.
  - KG-TandaFinal-Tramo1-r2b-sincola: M4 3.463525, M9 13 nodos aislados, M10 14 / 601.
  - KG-Acumulado-Tandas0y1yFinal-r2b: M4 5.997547, M9 51 nodos aislados, M10 1 / 10685.
  - KG-Acumulado-Tandas0y1yFinal-r2b-sincola: M4 5.588221, M9 48 nodos aislados, M10 192 / 10685.
  - KG-Acumulado-Tandas0y1yTramo1-r2b: M4 5.661442, M9 25 nodos aislados, M10 1 / 6335.
  - KG-Acumulado-Tandas0y1yTramo1-r2b-sincola: M4 5.176973, M9 25 nodos aislados, M10 125 / 6335.
- **Los contadores de E1 (informativos):** {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 0}.
- **Los `nombres_remision` medidos** (`nombres_remision/tabla_nombres_t3_tf.json`): iguales a la medición de la mesa en los cuatro ensamblados: True; la variante en cada manifiesto sigue la §19: KG-TandaFinal-r2b True; KG-TandaFinal-Tramo1-r2b True; KG-Acumulado-Tandas0y1yFinal-r2b True; KG-Acumulado-Tandas0y1yTramo1-r2b True.

**Veredicto del gate, con las decisiones de la §29 y la R23 y la V23 declaradas: PASA.**
