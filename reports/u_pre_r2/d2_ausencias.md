# U-PRE-R2-DIAG — D2: cruce de las ausencias con los candidatos del laudo

Mandato `docs/mandatos/UPRE_R2_diagnostico.md`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d2_ausencias.py --out-dir reports/u_pre_r2`. Todo número de este archivo sale de `d2_ausencias.json` (misma corrida). EV2 y sus trazas se usan como material de desarrollo para diagnosticar y priorizar; nada de esto es un resultado de r2 sobre EV2.

## 1. Decisiones de la autora al cierre de D1 y declaración

- Regla de presencia del ancla: la de regla_atribucion.md tal como está sellada (:83, coincidencia exacta, sin descendientes). La frase «y sus descendientes» de la decisión 8 del mandato fue un error del mandato.
- C1: pares y clase A0.2 desde data/experiment/ev2_r1/cierre/cierre_r1.json (774acac), la misma fuente que usó E6 para c1.lectura_plan_punto_3; la clase por par está en el archivo (atribucion.pares_definitivos.por_par): no se recomputó.
- Nota aparte sobre T2 (fusión de ext::7.5.3 y ext::7.8.5.1), clasificación asistida con el texto de E0 como evidencia.

## 2. Reglas declaradas antes de aplicarse

- **R-CITA**: números (porcentajes, fechas, plazos), siglas y palabras de 5 letras o más fuera de palabras vacías, normalizados; contiene si están todos los números y siglas y al menos 80 % de las palabras; parcial si al menos 50 % sin lo anterior; lo parcial es «requiere lectura»
- **R-UBIC**: unidades de E0 del subárbol del ancla con la cita en el texto propio; si ninguna, en el texto heredado desde el subárbol; si ninguna, fuera del subárbol (candidato D, requiere lectura)
- **R-PRES**: nodo que contiene la cita y ancla en el subárbol del ancla; contenedor = más de 10 anclas distintas
- **R-CAT**: P si está en un nodo no contenedor con aristas; C si solo en nodos sin aristas; F si solo en contenedores; si no está: E (unidad con error, corte o sin salida final; o tabular sin la cita en E1), G (la salida de E1 no la tiene), F (el nodo de su slug no la tiene), H (el nodo de su slug no está); antes de G, cita repartida entre varios nodos o entidades de la unidad y en ninguno solo → requiere lectura; secundarias B (relación de esa entidad rechazada por firma_invalida), E-tabla y E-tabla-no-marcada (unidad no marcada tabular por E0 con 3 o más líneas que empiezan con un código de 6 dígitos o más); fila = primera en el orden E, G, B, F, C, D, H, P
- **desvio_declarado**: la regla de contenido repartido y la secundaria E-tabla-no-marcada se agregaron después de una corrida de prueba en el scratchpad, que había marcado G en EV2F-025 criterio 4 de r1 (contenido emitido en dos entidades) y en EV2F-032 criterio 5 (cuadro de códigos que E0 no marca como tabular); R-CITA y sus umbrales no cambiaron

Categorías: **E** el chunk del ancla no se extrajo o se cortó, o su contenido es una tabla linealizada; **G** E1 no lo emitió: sin rastro en su salida; **B** E1 lo emitió y la matriz rechazó su relación por firma_invalida; **F** quedó fundido o duplicado en otro nodo; **C** está en el grafo sin la arista que lo conecta; **D** depende de una remisión no resuelta o falsa; **H** no decidible con el material; **P** fuera de la lista de la decisión 7: el contenido está en el grafo bajo una ancla descendiente; no hay pérdida en el pipeline.

Registros de rechazo:
- desarrollo: validacion.rechazos en corpus_tanda0/salida_dirigida/<to>/extracciones_e1.jsonl (la misma población que reports/u_audit_tipos_v3/p4_filas.json, 982 filas); población final por unidad en reports/u_estudio_matriz/uestmat_poblacion_final.json
- r1: validacion.rechazos en corpus_v2/salida/<to>/extracciones_e1.jsonl y extracciones_finales_<to>.jsonl (existen); equivalente de p4_filas.json o de uestmat_poblacion_final.json para r1: NO ENCONTRADO
- reintentos_crudos: data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db abierta con file:…?immutable=1; se consulta solo para unidades portadoras con estado_e3 aceptado_tras_reintento (namespace v3 en desarrollo; los otros en r1)

## 3. Entradas y población

| clave | ruta | sha256 |
|---|---|---|
| kg_r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d…` |
| kg_desarrollo | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad…` |
| cierre_r1_C1 | `data/experiment/ev2_r1/cierre/cierre_r1.json` | `665b39e958176b07…` |
| atribucion_tanda0 | `reports/tanda0/atribucion_tanda0.json` | `00b3c0a738b1d0de…` |
| definitivos_tanda0 | `data/experiment/ev2_tanda0/adjudicacion_SOLO_MESA/definitivos_por_par_tanda0_SOLO_MESA.json` | `e60a944ba580030a…` |
| gold_ev2 | `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` | `1d58733699c325c9…` |
| regla_atribucion | `data/experiment/ev2_reporte/regla_atribucion.md` | `20040e94c383286c…` |
| laudo_r2 | `docs/laudo_release_r2_pipeline.md` | `1820d26202c7b0a6…` |
| p4_filas_rechazos_desarrollo | `reports/u_audit_tipos_v3/p4_filas.json` | `61d765d467aea83c…` |
| uestmat_poblacion_final | `reports/u_estudio_matriz/uestmat_poblacion_final.json` | `299c45211bcf714d…` |
| e1_reintentos_db | `data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db` | `e71380308cbe3dde…` |

- Población recomputada por par: {'C1': 8, 'C2': 6, 'C3': 8, 'C4': 9} = 31; 9 anclas distintas (cap:2.11, cap:5.2.1, cla:2.1, ext:3.17, ext:5.10, ext:5.7, ric:5.2, ric:7.2, ric:9.2).
- E0 de los cinco TOs idéntico entre `salida_tanda0` y `salida_enm01`: {'pro': True, 'cla': True, 'ric': True, 'cap': True, 'ext': True}.
- Unidades consultadas en `e1_reintentos.db` (reintentos encontrados): {'r1': {'cla::2.1.1': 1}, 'desarrollo': {}}.

## 4. Tabla de prioridad

Por categoría (una fila por ausencia; primaria y primaria o secundaria):

| categoría | ausencias como primaria | celdas | ausencias como primaria o secundaria | celdas |
|---|---|---|---|---|
| B | 0 | — | 3 | C3, C4 |
| E-tabla | 4 | C1, C2, C3, C4 | 4 | C1, C2, C3, C4 |
| E-tabla-no-marcada | 0 | — | 4 | C1, C2, C3, C4 |
| G | 4 | C1, C2, C3, C4 | 4 | C1, C2, C3, C4 |
| P | 23 | C1, C2, C3, C4 | 23 | C1, C2, C3, C4 |

Suma de primarias: 31 (cierra en 31: sí).

Por candidato del laudo:

| candidato | ausencias como primaria | celdas | ausencias como primaria o secundaria | celdas |
|---|---|---|---|---|
| decisión sobre la matriz congelada (checklist X1 y X11); fuera del §1 | 0 | — | 3 | C3, C4 |
| fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 23 | C1, C2, C3, C4 | 23 | C1, C2, C3, C4 |
| fuera de r2 (toca el prompt de E1; «Qué no es» del laudo) | 4 | C1, C2, C3, C4 | 4 | C1, C2, C3, C4 |
| §1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0) | 4 | C1, C2, C3, C4 | 4 | C1, C2, C3, C4 |
| §1.3 BKL-0006 / RX-10, si la unidad que E0 no marca como tabular se trata como tabla | 0 | — | 4 | C1, C2, C3, C4 |

## 5. Una fila por ausencia

| celda | pregunta | ancla | definitivo | criterios no cubiertos | primaria | secundarias | candidato | ancla (descendientes) | ancla en la otra generación | contenido en la otra generación | requiere lectura |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | EV2F-002 | ext:5.10 | parcial | 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (13) | desarrollo: no | 2/2 | — |
| C1 | EV2F-009 | ext:5.7 | parcial | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (19) | desarrollo: no | 4/4 | — |
| C1 | EV2F-013 | ext:3.17 | parcial | 1, 2 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (59) | desarrollo: no | 2/2 | — |
| C1 | EV2F-017 | cap:5.2.1 | incorrecto | 1, 2, 3, 4, 5 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (16) | desarrollo: no | 5/5 | — |
| C1 | EV2F-024 | cap:2.11 | parcial | 1, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (28) | desarrollo: no | 3/3 | — |
| C1 | EV2F-025 | cla:2.1 | incorrecto | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (21) | desarrollo: no | 4/4 | 1, 4 |
| C1 | EV2F-031 | ric:7.2 | incorrecto | 1, 2, 3, 4 | E-tabla | — | §1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0) | 0 (0) | desarrollo: no | 0/4 | — |
| C1 | EV2F-032 | ric:9.2 | parcial | 5 | G | E-tabla-no-marcada | fuera de r2 (toca el prompt de E1; «Qué no es» del laudo) | 0 (7) | desarrollo: no | 0/1 | — |
| C2 | EV2F-013 | ext:3.17 | parcial | 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (59) | desarrollo: no | 3/3 | — |
| C2 | EV2F-017 | cap:5.2.1 | incorrecto | 1, 2, 3, 4, 5 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (16) | desarrollo: no | 5/5 | — |
| C2 | EV2F-024 | cap:2.11 | incorrecto | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (28) | desarrollo: no | 4/4 | — |
| C2 | EV2F-025 | cla:2.1 | incorrecto | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (21) | desarrollo: no | 4/4 | 1, 4 |
| C2 | EV2F-031 | ric:7.2 | incorrecto | 1, 2, 3, 4 | E-tabla | — | §1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0) | 0 (0) | desarrollo: no | 0/4 | — |
| C2 | EV2F-032 | ric:9.2 | parcial | 5 | G | E-tabla-no-marcada | fuera de r2 (toca el prompt de E1; «Qué no es» del laudo) | 0 (7) | desarrollo: no | 0/1 | — |
| C3 | EV2F-009 | ext:5.7 | parcial | 2 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (20) | r1: no | 1/1 | — |
| C3 | EV2F-013 | ext:3.17 | parcial | 1, 2, 3 | P | B | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (61) | r1: no | 3/3 | — |
| C3 | EV2F-017 | cap:5.2.1 | incorrecto | 1, 2, 3, 4, 5 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (17) | r1: no | 5/5 | — |
| C3 | EV2F-024 | cap:2.11 | parcial | 2, 3, 4 | P | B | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (22) | r1: no | 3/3 | — |
| C3 | EV2F-025 | cla:2.1 | incorrecto | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (13) | r1: no | 2/4 | — |
| C3 | EV2F-031 | ric:7.2 | incorrecto | 1, 2, 3, 4 | E-tabla | — | §1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0) | 0 (0) | r1: no | 0/4 | — |
| C3 | EV2F-032 | ric:9.2 | parcial | 5 | G | E-tabla-no-marcada | fuera de r2 (toca el prompt de E1; «Qué no es» del laudo) | 0 (5) | r1: no | 0/1 | — |
| C3 | EV2F-035 | ric:5.2 | parcial | 1 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (24) | r1: no | 1/1 | — |
| C4 | EV2F-002 | ext:5.10 | parcial | 2 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (13) | r1: no | 1/1 | — |
| C4 | EV2F-009 | ext:5.7 | parcial | 3 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (20) | r1: no | 1/1 | — |
| C4 | EV2F-013 | ext:3.17 | incorrecto | 1, 2, 3, 4 | P | B | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (61) | r1: no | 4/4 | — |
| C4 | EV2F-017 | cap:5.2.1 | incorrecto | 1, 2, 3, 4, 5 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (17) | r1: no | 5/5 | — |
| C4 | EV2F-024 | cap:2.11 | parcial | 1, 2, 3 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (22) | r1: no | 3/3 | — |
| C4 | EV2F-025 | cla:2.1 | incorrecto | 1, 2, 3, 4 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (13) | r1: no | 2/4 | — |
| C4 | EV2F-031 | ric:7.2 | incorrecto | 1, 2, 3, 4 | E-tabla | — | §1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0) | 0 (0) | r1: no | 0/4 | — |
| C4 | EV2F-032 | ric:9.2 | parcial | 5 | G | E-tabla-no-marcada | fuera de r2 (toca el prompt de E1; «Qué no es» del laudo) | 0 (5) | r1: no | 0/1 | — |
| C4 | EV2F-035 | ric:5.2 | parcial | 1 | P | — | fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2) | 0 (24) | r1: no | 1/1 | — |

Diagnóstico descriptivo del ancla (no es categoría; resolucion.AnclaIndex con y sin descendientes y contenedores): cap:2.11 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; cap:2.11 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; cap:5.2.1 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; cap:5.2.1 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; cla:2.1 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; cla:2.1 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:3.17 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:3.17 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:5.10 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:5.10 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:5.7 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ext:5.7 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ric:5.2 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ric:7.2 en desarrollo: sin nodos de contenido: solo el nodo TextoOrdenado (contenedor) porta el ancla; ric:7.2 en r1: sin nodos de contenido: solo el nodo TextoOrdenado (contenedor) porta el ancla; ric:9.2 en desarrollo: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes; ric:9.2 en r1: granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes.

Evidencia de cada fila: `d2_ausencias.json`, `filas[]` (clave `evidencia`), con el diagnóstico por criterio (`criterios[].diagnostico`: unidades de E0, nodos con la cita, estado de las unidades portadoras con archivo:línea de sus registros de E1, nodo del slug y rechazos).

### Detalle por criterio

| celda | pregunta | criterio | categoría | motivo | unidades E0 (propias / herencia) | nodos con la cita (grado, contenedor) |
|---|---|---|---|---|---|---|
| C1 | EV2F-002 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.10.2 / — | Obligacion_las_operaciones_propias_de_la… (g3) |
| C1 | EV2F-002 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.10.3 / — | Restriccion_no_correspondera_realizar_re… (g3) |
| C1 | EV2F-009 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.7.1 / — | Excepcion_se_admitira_la_utilizacion_del… (g1, parcial); Obligacion_la_entidad_debera_registrar_a… (g4); Operacion_registro_operacion_mercado_de_… (g2, parcial) |
| C1 | EV2F-009 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.7.2 / — | Obligacion_el_registro_de_esas_operacion… (g3) |
| C1 | EV2F-009 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | — / ext::5.7.3::intro, ext::5.7.3.1, ext::5.7.3.2, ext::5.7.3.3, ext::5.7.3.4 | Obligacion_a_esos_efectos_se_utilizara_c… (g3); Obligacion_se_utilizara_cuit_cuil_cdi_ci… (g4); Operacion_operacion_con_cliente_en_cambi… (g2, parcial) |
| C1 | EV2F-009 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.7.3.1 / — | Excepcion_en_las_situaciones_que_se_deta… (g2) |
| C1 | EV2F-013 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1::intro / ext::3.17.1.1, ext::3.17.1.2, ext::3.17.1.3, ext::3.17.1.4, ext::3.17.1.5, ext::3.17.1.6, ext::3.17.2::intro, ext::3.17.2.1, ext::3.17.2.2 | Obligacion_el_cliente_que_cuente_con_una… (g2); Obligacion_los_beneficiarios_del_regimen… (g3, parcial); Operacion_acceso_mercado_cambios_con_cer… (g2, parcial) |
| C1 | EV2F-013 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.1 / — | Restriccion_pagos_de_capital_de_deudas_o… (g2); Restriccion_pagos_de_capital_de_deudas_o… (g6, parcial) |
| C1 | EV2F-017 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.1 / — | Obligacion_la_documentacion_vinculada_co… (g2) |
| C1 | EV2F-017 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.3 / — | Restriccion_no_debera_existir_una_correl… (g4) |
| C1 | EV2F-017 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.4 / — | Restriccion_ninguna_exposicion_creditici… (g3) |
| C1 | EV2F-017 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.5 / — | Obligacion_calcular_por_separado_los_act… (g3); Obligacion_la_entidad_financiera_que_cue… (g3, parcial) |
| C1 | EV2F-017 | 5 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.6 / — | Obligacion_las_entidades_deben_utilizar_… (g3, parcial); Restriccion_la_reduccion_o_transferencia… (g2) |
| C1 | EV2F-024 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.1, cap::2.11.2 / — | Obligacion_las_entidades_financieras_del… (g3, parcial); Obligacion_las_entidades_financieras_del… (g3); Obligacion_las_entidades_financieras_del… (g3) |
| C1 | EV2F-024 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.1 / — | Restriccion_participaciones_directas_e_i… (g3) |
| C1 | EV2F-024 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.2 / — | Obligacion_instrumentos_representan_un_d… (g2) |
| C1 | EV2F-025 | 1 | requiere_lectura | la salida de E1 contiene la cita solo parcialmente | cla::2.1.1 / — | Obligacion_creditos_diversos_capitales_e… (g3, parcial); Operacion_inclusion_en_clasificacion_pre… (g2, parcial); Restriccion_otros_creditos_por_intermedi… (g3, parcial) |
| C1 | EV2F-025 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.3 / — | Obligacion_creditos_diversos_capitales_e… (g3, parcial); Restriccion_los_creditos_por_arrendamien… (g3); Restriccion_otros_creditos_por_intermedi… (g3, parcial) |
| C1 | EV2F-025 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.5.2 / — | Operacion_avales_otorgados_sobre_cheques… (g1) |
| C1 | EV2F-025 | 4 | requiere_lectura | la cita está repartida entre varios nodos de la unidad portadora (ningún nodo la contiene solo) | cla::2.1.6 / — | — |
| C1 | EV2F-031 | 1 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C1 | EV2F-031 | 2 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C1 | EV2F-031 | 3 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C1 | EV2F-031 | 4 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C1 | EV2F-032 | 5 | G | la salida de E1 de las unidades portadoras no contiene la cita | ric::9.2.1 / — | — |
| C2 | EV2F-013 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.1 / — | Restriccion_pagos_de_capital_de_deudas_o… (g2); Restriccion_pagos_de_capital_de_deudas_o… (g6, parcial) |
| C2 | EV2F-013 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.4 / — | Operacion_pagos_utilidades_dividendos_ac… (g1); Restriccion_el_monto_equivalente_de_los_… (g10, parcial); Restriccion_pagos_de_utilidades_y_divide… (g10) |
| C2 | EV2F-013 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.2::intro / ext::3.17.2.1, ext::3.17.2.2 | Obligacion_los_beneficiarios_del_regimen… (g3) |
| C2 | EV2F-017 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.1 / — | Obligacion_la_documentacion_vinculada_co… (g2) |
| C2 | EV2F-017 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.3 / — | Restriccion_no_debera_existir_una_correl… (g4) |
| C2 | EV2F-017 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.4 / — | Restriccion_ninguna_exposicion_creditici… (g3) |
| C2 | EV2F-017 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.5 / — | Obligacion_calcular_por_separado_los_act… (g3); Obligacion_la_entidad_financiera_que_cue… (g3, parcial) |
| C2 | EV2F-017 | 5 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.6 / — | Obligacion_las_entidades_deben_utilizar_… (g3, parcial); Restriccion_la_reduccion_o_transferencia… (g2) |
| C2 | EV2F-024 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.1, cap::2.11.2 / — | Obligacion_las_entidades_financieras_del… (g3, parcial); Obligacion_las_entidades_financieras_del… (g3); Obligacion_las_entidades_financieras_del… (g3) |
| C2 | EV2F-024 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3::intro / cap::2.11.3.1, cap::2.11.3.2, cap::2.11.3.3, cap::2.11.3.4, cap::2.11.3.5 | Obligacion_a_los_fines_de_determinar_si_… (g4); Obligacion_las_entidades_financieras_del… (g3) |
| C2 | EV2F-024 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.1 / — | Restriccion_participaciones_directas_e_i… (g3) |
| C2 | EV2F-024 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.2 / — | Obligacion_instrumentos_representan_un_d… (g2) |
| C2 | EV2F-025 | 1 | requiere_lectura | la salida de E1 contiene la cita solo parcialmente | cla::2.1.1 / — | Obligacion_creditos_diversos_capitales_e… (g3, parcial); Operacion_inclusion_en_clasificacion_pre… (g2, parcial); Restriccion_otros_creditos_por_intermedi… (g3, parcial) |
| C2 | EV2F-025 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.3 / — | Obligacion_creditos_diversos_capitales_e… (g3, parcial); Restriccion_los_creditos_por_arrendamien… (g3); Restriccion_otros_creditos_por_intermedi… (g3, parcial) |
| C2 | EV2F-025 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.5.2 / — | Operacion_avales_otorgados_sobre_cheques… (g1) |
| C2 | EV2F-025 | 4 | requiere_lectura | la cita está repartida entre varios nodos de la unidad portadora (ningún nodo la contiene solo) | cla::2.1.6 / — | — |
| C2 | EV2F-031 | 1 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C2 | EV2F-031 | 2 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C2 | EV2F-031 | 3 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C2 | EV2F-031 | 4 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C2 | EV2F-032 | 5 | G | la salida de E1 de las unidades portadoras no contiene la cita | ric::9.2.1 / — | — |
| C3 | EV2F-009 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.7.2 / — | Obligacion_el_registro_de_esas_operacion… (g3); Operacion_registro_de_operaciones_cambia… (g1) |
| C3 | EV2F-013 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1::intro / ext::3.17.1.1, ext::3.17.1.2, ext::3.17.1.3, ext::3.17.1.4, ext::3.17.1.5, ext::3.17.1.6, ext::3.17.2::intro, ext::3.17.2.1, ext::3.17.2.2 | Condicion_certificacion_decreto_277_22_p… (g1); Obligacion_la_entidad_financiera_local_n… (g2, parcial); Obligacion_los_beneficiarios_del_radpip_… (g2, parcial) |
| C3 | EV2F-013 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.1 / — | Operacion_pago_de_capital_de_deuda_por_i… (g5, parcial); Operacion_pagos_de_capital_deudas_import… (g3) |
| C3 | EV2F-013 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.4 / — | Definicion_deduccion_por_pagos_de_utilid… (g2, parcial); Operacion_pagos_de_utilidades_y_dividend… (g8) |
| C3 | EV2F-017 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.1 / — | Obligacion_la_documentacion_vinculada_co… (g2); Obligacion_las_entidades_financieras_deb… (g2, parcial) |
| C3 | EV2F-017 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.3 / — | Restriccion_no_debera_existir_una_correl… (g4) |
| C3 | EV2F-017 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.4 / — | Restriccion_ninguna_exposicion_creditici… (g3) |
| C3 | EV2F-017 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.5 / — | Obligacion_la_entidad_financiera_que_cue… (g4); Operacion_division_de_exposicion_entre_t… (g2) |
| C3 | EV2F-017 | 5 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.6 / — | Condicion_incremento_de_riesgos_residual… (g2); Obligacion_las_entidades_deben_utilizar_… (g3, parcial) |
| C3 | EV2F-024 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3::intro / cap::2.11.3.1, cap::2.11.3.2, cap::2.11.3.3, cap::2.11.3.4, cap::2.11.3.5 | Obligacion_las_entidades_financieras_del… (g4) |
| C3 | EV2F-024 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.1 / — | Definicion_exposicion_a_acciones_partici… (g1) |
| C3 | EV2F-024 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.2 / — | Condicion_derecho_residual_sobre_activos… (g0); Definicion_instrumentos_calificables_com… (g1) |
| C3 | EV2F-025 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.1 / — | Definicion_creditos_diversos_venta_de_ac… (g1, parcial); Definicion_otros_creditos_por_intermedia… (g1, parcial); Definicion_prestamos_incluidos_en_activo… (g1) |
| C3 | EV2F-025 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.3 / — | Definicion_creditos_diversos_venta_de_ac… (g1, parcial); Definicion_otros_creditos_por_intermedia… (g1, parcial); Operacion_creditos_por_arrendamientos_fi… (g1) |
| C3 | EV2F-025 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.5.2 / — | Operacion_avales_sobre_cheques_de_pago_d… (g1) |
| C3 | EV2F-025 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.6 / — | Definicion_obligaciones_negociables_y_ti… (g1) |
| C3 | EV2F-031 | 1 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C3 | EV2F-031 | 2 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C3 | EV2F-031 | 3 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C3 | EV2F-031 | 4 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C3 | EV2F-032 | 5 | G | la salida de E1 de las unidades portadoras no contiene la cita | ric::9.2.1 / — | Operacion_informacion_de_incumplimientos… (g1, parcial); Operacion_informacion_de_incumplimientos… (g1, parcial); Operacion_informacion_de_incumplimientos… (g1, parcial) |
| C3 | EV2F-035 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ric::5.2.1 / — | Obligacion_se_informara_el_bic_calculado… (g3); Obligacion_se_informara_el_ingreso_bruto… (g3, parcial); Operacion_calculo_e_informacion_del_bic_… (g2) |
| C4 | EV2F-002 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::5.10.1.2 / — | Obligacion_las_entidades_deberan_confecc… (g3, parcial); Obligacion_las_entidades_deberan_confecc… (g3); Operacion_operaciones_de_cambio_canje_o_… (g3) |
| C4 | EV2F-009 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | — / ext::5.7.3::intro, ext::5.7.3.1, ext::5.7.3.2, ext::5.7.3.3, ext::5.7.3.4 | Obligacion_se_utilizara_cuit_cuil_cdi_ci… (g5); Operacion_operacion_en_mercado_de_cambio… (g2, parcial); Operacion_registro_de_operacion_con_clie… (g3, parcial) |
| C4 | EV2F-013 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1::intro / ext::3.17.1.1, ext::3.17.1.2, ext::3.17.1.3, ext::3.17.1.4, ext::3.17.1.5, ext::3.17.1.6, ext::3.17.2::intro, ext::3.17.2.1, ext::3.17.2.2 | Condicion_certificacion_decreto_277_22_p… (g1); Obligacion_la_entidad_financiera_local_n… (g2, parcial); Obligacion_los_beneficiarios_del_radpip_… (g2, parcial) |
| C4 | EV2F-013 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.1 / — | Operacion_pago_de_capital_de_deuda_por_i… (g5, parcial); Operacion_pagos_de_capital_deudas_import… (g3) |
| C4 | EV2F-013 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.1.4 / — | Definicion_deduccion_por_pagos_de_utilid… (g2, parcial); Operacion_pagos_de_utilidades_y_dividend… (g8) |
| C4 | EV2F-013 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ext::3.17.2::intro / ext::3.17.2.1, ext::3.17.2.2 | Obligacion_la_entidad_financiera_local_n… (g2, parcial); Obligacion_los_beneficiarios_del_radpip_… (g2); Obligacion_los_beneficiarios_del_regimen… (g2, parcial) |
| C4 | EV2F-017 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.1 / — | Obligacion_la_documentacion_vinculada_co… (g2); Obligacion_las_entidades_financieras_deb… (g2, parcial) |
| C4 | EV2F-017 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.3 / — | Restriccion_no_debera_existir_una_correl… (g4) |
| C4 | EV2F-017 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.4 / — | Restriccion_ninguna_exposicion_creditici… (g3) |
| C4 | EV2F-017 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.5 / — | Obligacion_la_entidad_financiera_que_cue… (g4); Operacion_division_de_exposicion_entre_t… (g2) |
| C4 | EV2F-017 | 5 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::5.2.1.6 / — | Condicion_incremento_de_riesgos_residual… (g2); Obligacion_las_entidades_deben_utilizar_… (g3, parcial) |
| C4 | EV2F-024 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.1, cap::2.11.2 / — | Definicion_exposicion_a_acciones_partici… (g1, parcial); Obligacion_las_entidades_financieras_del… (g3); Obligacion_las_entidades_financieras_del… (g3, parcial) |
| C4 | EV2F-024 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3::intro / cap::2.11.3.1, cap::2.11.3.2, cap::2.11.3.3, cap::2.11.3.4, cap::2.11.3.5 | Obligacion_las_entidades_financieras_del… (g4) |
| C4 | EV2F-024 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cap::2.11.3.1 / — | Definicion_exposicion_a_acciones_partici… (g1) |
| C4 | EV2F-025 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.1 / — | Definicion_creditos_diversos_venta_de_ac… (g1, parcial); Definicion_otros_creditos_por_intermedia… (g1, parcial); Definicion_prestamos_incluidos_en_activo… (g1) |
| C4 | EV2F-025 | 2 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.3 / — | Definicion_creditos_diversos_venta_de_ac… (g1, parcial); Definicion_otros_creditos_por_intermedia… (g1, parcial); Operacion_creditos_por_arrendamientos_fi… (g1) |
| C4 | EV2F-025 | 3 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.5.2 / — | Operacion_avales_sobre_cheques_de_pago_d… (g1) |
| C4 | EV2F-025 | 4 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | cla::2.1.6 / — | Definicion_obligaciones_negociables_y_ti… (g1) |
| C4 | EV2F-031 | 1 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C4 | EV2F-031 | 2 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C4 | EV2F-031 | 3 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C4 | EV2F-031 | 4 | E-tabla | unidad portadora tabular en E0 y sin la cita en la salida de E1: ['ric::7.2'] | ric::7.2 / — | — |
| C4 | EV2F-032 | 5 | G | la salida de E1 de las unidades portadoras no contiene la cita | ric::9.2.1 / — | Operacion_informacion_de_incumplimientos… (g1, parcial); Operacion_informacion_de_incumplimientos… (g1, parcial); Operacion_informacion_de_incumplimientos… (g1, parcial) |
| C4 | EV2F-035 | 1 | P | contenido presente en un nodo con aristas bajo el subárbol del ancla | ric::5.2.1 / — | Obligacion_se_informara_el_bic_calculado… (g3); Obligacion_se_informara_el_ingreso_bruto… (g3, parcial); Operacion_calculo_e_informacion_del_bic_… (g2) |

## 6. Requiere lectura y no decidibles

Requiere lectura (2 filas; quién lee lo decide la autora, checklist P15 y Q12):
- C1 EV2F-025 (cla:2.1): criterio 1: la salida de E1 contiene la cita solo parcialmente; criterio 4: la cita está repartida entre varios nodos de la unidad portadora (ningún nodo la contiene solo)
- C2 EV2F-025 (cla:2.1): criterio 1: la salida de E1 contiene la cita solo parcialmente; criterio 4: la cita está repartida entre varios nodos de la unidad portadora (ningún nodo la contiene solo)

No decidibles, H (0 filas): ninguna.

## 7. Nota aparte: T2 (clasificación asistida)

Pregunta: ¿las dos restricciones fundidas en KG-Tanda0-Desarrollo-r1 son la misma regla repetida en dos puntos o reglas distintas con la misma redacción?

- `ext::7.5.3` (E0, sha256 completo `237e5dd517f7…`), contiene la oración del 125 % (espacios normalizados): sí. Texto propio previo a «Esta opción»: «7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- `ext::7.8.5.1` (E0, sha256 completo `1cbcc6d0e654…`), contiene la oración del 125 % (espacios normalizados): sí. Texto propio previo a «Esta opción»: «7.8.5.1. acumular los fondos originados en el cobro de exportaciones de bienes y servicios del deudor en cuentas en moneda extranjera abiertas en entidades financieras locales o en el exterior destinadas a garantizar la cancelación de los vencimientos de dicha prefinanciación según lo previsto en el contrato de financiamiento.»

**Clasificación asistida: reglas distintas con la misma redacción.** Lectura de esta instancia, para revisión de la autora. La oración del 125 % es idéntica en los dos puntos, pero «Esta opción» remite a opciones distintas. En ext::7.5.3 la opción es la ampliación del plazo de liquidación de divisas del permiso hasta el quinto día hábil posterior a la fecha en que los cobros deben permanecer depositados; el tope del 125 % limita esa ampliación. En ext::7.8.5.1 la opción es acumular los fondos del cobro de exportaciones en cuentas en moneda extranjera en garantía de la prefinanciación; el tope limita esa acumulación, y el punto agrega que los fondos excedentes se liquidan en los plazos generales. Los dos puntos están relacionados (7.5.3 menciona las prefinanciaciones del 7.8.5), pero el objeto del tope es distinto: el nodo fundido pierde de qué opción se trata.
