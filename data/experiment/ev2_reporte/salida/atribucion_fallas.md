# Atribución determinística de fallas — EV2 (U-A0 / A0.2)

Generado 2026-08-17T18:21:09. Regla: `data/experiment/ev2_reporte/regla_atribucion.md` (sha256 `20040e94c383…`, commit `40603a9`). USD 0, sin API. Determinístico.

Grafos (nombre canónico, sha256): KG-Base `12c226e2` (`data/experiment/run_3_ppf_core/kg.json`); KG-Refinado `26fac8b4` (`data/experiment/grafo_v2/reensamblado_v3/kg.json`); KG-Reextraído `8e2eadee` (`data/experiment/reextraccion_v2/corpus_v2/salida/kg.json`).

Replay: 120/120 trazas con replay estándar OK y 120/120 con replay fuerte OK.

## 1. Corrida base (120 trazas, veredicto de ESA respuesta: juez base + adjudicación de los heredados)

### 1.a Clase × grafo

| grafo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto (no atribuible) | n |
|---|---|---|---|---|---|---|
| KG-Base | 6 | 11 | 3 | 17 | 3 | 40 |
| KG-Refinado | 4 | 6 | 1 | 25 | 4 | 40 |
| KG-Reextraído | 9 | 1 | 5 | 21 | 4 | 40 |

### 1.b Clase × grafo × veredicto

| grafo | veredicto | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | correcto | 0 | 0 | 0 | 0 | 3 |
| KG-Base | incorrecto | 3 | 8 | 2 | 1 | 0 |
| KG-Base | parcial | 3 | 3 | 1 | 16 | 0 |
| KG-Refinado | correcto | 0 | 0 | 0 | 0 | 4 |
| KG-Refinado | incorrecto | 0 | 3 | 1 | 2 | 0 |
| KG-Refinado | parcial | 4 | 3 | 0 | 23 | 0 |
| KG-Reextraído | correcto | 0 | 0 | 0 | 0 | 4 |
| KG-Reextraído | incorrecto | 4 | 0 | 1 | 3 | 0 |
| KG-Reextraído | parcial | 5 | 1 | 4 | 18 | 0 |

### 1.c Clase × grafo × clasificación auxiliar del juez (columna cruzada)

| grafo | auxiliar | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | abstencion | 3 | 4 | 1 | 1 | 0 |
| KG-Base | contenido | 3 | 7 | 2 | 16 | 3 |
| KG-Refinado | abstencion | 0 | 2 | 0 | 2 | 0 |
| KG-Refinado | contenido | 4 | 4 | 1 | 23 | 4 |
| KG-Reextraído | abstencion | 2 | 0 | 1 | 4 | 0 |
| KG-Reextraído | contenido | 7 | 1 | 4 | 17 | 4 |

### 1.d Clase × grafo × flag `respondible` del agente (metadato)

| grafo | respondible | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | False | 3 | 8 | 1 | 3 | 0 |
| KG-Base | True | 3 | 3 | 2 | 14 | 3 |
| KG-Refinado | False | 1 | 2 | 0 | 4 | 0 |
| KG-Refinado | True | 3 | 4 | 1 | 21 | 4 |
| KG-Reextraído | False | 6 | 0 | 1 | 7 | 0 |
| KG-Reextraído | True | 3 | 1 | 4 | 14 | 4 |

### Criterios no cumplidos × grafo × clase (respuesta representativa = la propia)

| grafo | clase | n trazas | criterios | no cumplidos | media no cumplidos/traza | tasa no cumplidos |
|---|---|---|---|---|---|---|
| KG-Base | ausencia_kg | 6 | 24 | 18 | 3.0 | 0.75 |
| KG-Base | alcanzabilidad | 11 | 41 | 36 | 3.273 | 0.878 |
| KG-Base | vista_no_consultada | 3 | 13 | 12 | 4.0 | 0.9231 |
| KG-Base | generacion | 17 | 72 | 36 | 2.118 | 0.5 |
| KG-Base | correcto | 3 | 14 | 0 | 0.0 | 0.0 |
| KG-Refinado | ausencia_kg | 4 | 18 | 14 | 3.5 | 0.7778 |
| KG-Refinado | alcanzabilidad | 6 | 21 | 16 | 2.667 | 0.7619 |
| KG-Refinado | vista_no_consultada | 1 | 4 | 4 | 4.0 | 1.0 |
| KG-Refinado | generacion | 25 | 106 | 51 | 2.04 | 0.4811 |
| KG-Refinado | correcto | 4 | 15 | 0 | 0.0 | 0.0 |
| KG-Reextraído | ausencia_kg | 9 | 39 | 28 | 3.111 | 0.7179 |
| KG-Reextraído | alcanzabilidad | 1 | 4 | 3 | 3.0 | 0.75 |
| KG-Reextraído | vista_no_consultada | 5 | 20 | 12 | 2.4 | 0.6 |
| KG-Reextraído | generacion | 21 | 88 | 52 | 2.476 | 0.5909 |
| KG-Reextraído | correcto | 4 | 13 | 0 | 0.0 | 0.0 |

### 1.e Perfiles por pregunta (KG-Base / KG-Refinado / KG-Reextraído)

| perfil | n preguntas |
|---|---|
| generacion/generacion/generacion | 10 |
| alcanzabilidad/generacion/generacion | 3 |
| generacion/generacion/vista_no_consultada | 3 |
| ausencia_kg/ausencia_kg/generacion | 3 |
| generacion/generacion/ausencia_kg | 3 |
| vista_no_consultada/generacion/generacion | 2 |
| alcanzabilidad/generacion/vista_no_consultada | 2 |
| alcanzabilidad/alcanzabilidad/ausencia_kg | 2 |
| alcanzabilidad/correcto/ausencia_kg | 1 |
| generacion/generacion/correcto | 1 |
| vista_no_consultada/vista_no_consultada/ausencia_kg | 1 |
| alcanzabilidad/generacion/alcanzabilidad | 1 |
| ausencia_kg/alcanzabilidad/generacion | 1 |
| ausencia_kg/ausencia_kg/ausencia_kg | 1 |
| ausencia_kg/correcto/correcto | 1 |
| alcanzabilidad/alcanzabilidad/generacion | 1 |
| correcto/correcto/ausencia_kg | 1 |
| correcto/correcto/generacion | 1 |
| correcto/alcanzabilidad/correcto | 1 |
| alcanzabilidad/alcanzabilidad/correcto | 1 |

## 2. Re-corridas §7 (191 trazas atribuidas contra su propio veredicto; 7 excluidas sin veredicto propio)

### 2.a Clase × grafo

| grafo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto (no atribuible) | n |
|---|---|---|---|---|---|---|
| KG-Base | 8 | 1 | 2 | 42 | 3 | 56 |
| KG-Refinado | 12 | 7 | 1 | 39 | 6 | 65 |
| KG-Reextraído | 18 | 3 | 5 | 39 | 5 | 70 |

### 2.b Clase × grafo × veredicto

| grafo | veredicto | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | correcto | 0 | 0 | 0 | 0 | 3 |
| KG-Base | incorrecto | 2 | 1 | 0 | 5 | 0 |
| KG-Base | parcial | 6 | 0 | 2 | 37 | 0 |
| KG-Refinado | correcto | 0 | 0 | 0 | 0 | 6 |
| KG-Refinado | incorrecto | 5 | 2 | 0 | 0 | 0 |
| KG-Refinado | parcial | 7 | 5 | 1 | 39 | 0 |
| KG-Reextraído | correcto | 0 | 0 | 0 | 0 | 5 |
| KG-Reextraído | incorrecto | 0 | 2 | 0 | 0 | 0 |
| KG-Reextraído | parcial | 18 | 1 | 5 | 39 | 0 |

### 2.c Clase × grafo × clasificación auxiliar

| grafo | auxiliar | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | abstencion | 2 | 0 | 0 | 2 | 0 |
| KG-Base | contenido | 6 | 1 | 2 | 40 | 3 |
| KG-Refinado | abstencion | 2 | 3 | 1 | 0 | 0 |
| KG-Refinado | contenido | 10 | 4 | 0 | 39 | 6 |
| KG-Reextraído | contenido | 18 | 3 | 5 | 39 | 5 |

### Criterios no cumplidos × grafo × clase (respuesta representativa = la propia)

| grafo | clase | n trazas | criterios | no cumplidos | media no cumplidos/traza | tasa no cumplidos |
|---|---|---|---|---|---|---|
| KG-Base | ausencia_kg | 8 | 31 | 19 | 2.375 | 0.6129 |
| KG-Base | alcanzabilidad | 1 | 4 | 4 | 4.0 | 1.0 |
| KG-Base | vista_no_consultada | 2 | 8 | 6 | 3.0 | 0.75 |
| KG-Base | generacion | 42 | 177 | 93 | 2.214 | 0.5254 |
| KG-Base | correcto | 3 | 15 | 0 | 0.0 | 0.0 |
| KG-Refinado | ausencia_kg | 12 | 54 | 47 | 3.917 | 0.8704 |
| KG-Refinado | alcanzabilidad | 7 | 24 | 19 | 2.714 | 0.7917 |
| KG-Refinado | vista_no_consultada | 1 | 4 | 3 | 3.0 | 0.75 |
| KG-Refinado | generacion | 39 | 169 | 74 | 1.897 | 0.4379 |
| KG-Refinado | correcto | 6 | 19 | 0 | 0.0 | 0.0 |
| KG-Reextraído | ausencia_kg | 18 | 81 | 28 | 1.556 | 0.3457 |
| KG-Reextraído | alcanzabilidad | 3 | 12 | 11 | 3.667 | 0.9167 |
| KG-Reextraído | vista_no_consultada | 5 | 20 | 13 | 2.6 | 0.65 |
| KG-Reextraído | generacion | 39 | 160 | 78 | 2.0 | 0.4875 |
| KG-Reextraído | correcto | 5 | 22 | 0 | 0.0 | 0.0 |

## 3. Pares definitivos (120): clase de la traza representativa del veredicto definitivo

Regla ratificada de respuesta representativa (vías juez_base/adjudicacion_base → traza base; juez_enc/adjudicacion_s7 → re-corrida de menor rep cuyo veredicto propio coincide con el definitivo). Cada clase sigue siendo la de una traza contra su propio veredicto.

### 3.a Clase × grafo × veredicto DEFINITIVO

| grafo | definitivo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto |
|---|---|---|---|---|---|---|
| KG-Base | correcto | 0 | 0 | 0 | 0 | 3 |
| KG-Base | incorrecto | 4 | 8 | 2 | 3 | 0 |
| KG-Base | parcial | 2 | 3 | 0 | 15 | 0 |
| KG-Refinado | correcto | 0 | 0 | 0 | 0 | 5 |
| KG-Refinado | incorrecto | 2 | 4 | 1 | 2 | 0 |
| KG-Refinado | parcial | 2 | 3 | 0 | 21 | 0 |
| KG-Reextraído | correcto | 0 | 0 | 0 | 0 | 4 |
| KG-Reextraído | incorrecto | 4 | 1 | 1 | 3 | 0 |
| KG-Reextraído | parcial | 6 | 0 | 3 | 18 | 0 |

### 3.b Los incorrectos definitivos, uno por uno (traza representativa, clase, auxiliar)

| grafo | id_pregunta | vía | traza | clase | auxiliar |
|---|---|---|---|---|---|
| KG-Base | EV2F-001 | juez_base | base | alcanzabilidad | abstencion |
| KG-Base | EV2F-002 | juez_base | base | alcanzabilidad | contenido |
| KG-Base | EV2F-003 | juez_base | base | vista_no_consultada | abstencion |
| KG-Base | EV2F-007 | juez_base | base | vista_no_consultada | contenido |
| KG-Base | EV2F-008 | juez_enc | enc_r2 | ausencia_kg | abstencion |
| KG-Base | EV2F-011 | juez_base | base | generacion | abstencion |
| KG-Base | EV2F-012 | juez_base | base | alcanzabilidad | abstencion |
| KG-Base | EV2F-016 | juez_base | base | alcanzabilidad | contenido |
| KG-Base | EV2F-017 | juez_base | base | ausencia_kg | abstencion |
| KG-Base | EV2F-022 | juez_enc | enc_r1 | generacion | contenido |
| KG-Base | EV2F-023 | juez_base | base | ausencia_kg | abstencion |
| KG-Base | EV2F-025 | juez_base | base | alcanzabilidad | abstencion |
| KG-Base | EV2F-028 | juez_base | base | ausencia_kg | abstencion |
| KG-Base | EV2F-029 | juez_base | base | alcanzabilidad | contenido |
| KG-Base | EV2F-031 | juez_base | base | alcanzabilidad | abstencion |
| KG-Base | EV2F-036 | juez_enc | enc_r1 | generacion | contenido |
| KG-Base | EV2F-040 | juez_base | base | alcanzabilidad | contenido |
| KG-Refinado | EV2F-001 | juez_base | base | generacion | abstencion |
| KG-Refinado | EV2F-007 | juez_base | base | generacion | abstencion |
| KG-Refinado | EV2F-012 | adjudicacion_s7 | enc_r2 | alcanzabilidad | abstencion |
| KG-Refinado | EV2F-013 | juez_base | base | vista_no_consultada | contenido |
| KG-Refinado | EV2F-017 | adjudicacion_s7 | enc_r2 | ausencia_kg | abstencion |
| KG-Refinado | EV2F-023 | juez_enc | enc_r2 | ausencia_kg | contenido |
| KG-Refinado | EV2F-025 | juez_base | base | alcanzabilidad | contenido |
| KG-Refinado | EV2F-031 | juez_base | base | alcanzabilidad | abstencion |
| KG-Refinado | EV2F-040 | juez_base | base | alcanzabilidad | abstencion |
| KG-Reextraído | EV2F-001 | juez_base | base | generacion | abstencion |
| KG-Reextraído | EV2F-007 | juez_base | base | generacion | abstencion |
| KG-Reextraído | EV2F-012 | juez_base | base | vista_no_consultada | abstencion |
| KG-Reextraído | EV2F-014 | adjudicacion_s7 | enc_r1 | alcanzabilidad | contenido |
| KG-Reextraído | EV2F-017 | juez_base | base | ausencia_kg | contenido |
| KG-Reextraído | EV2F-023 | adjudicacion_base | base | generacion | abstencion |
| KG-Reextraído | EV2F-025 | juez_base | base | ausencia_kg | abstencion |
| KG-Reextraído | EV2F-026 | juez_base | base | ausencia_kg | contenido |
| KG-Reextraído | EV2F-031 | juez_base | base | ausencia_kg | abstencion |

## 4. Censo de las 40 anclas de fidelidad por grafo: anclas no resueltas y diagnóstico

| grafo | anclas no resueltas | diagnóstico | detalle (id: ancla, crudo/desc) |
|---|---|---|---|
| KG-Base | 6 | {'crudo=0,desc=0 (ausencia total)': 6} | EV2F-005: ext:4.6.1 0/0; EV2F-008: ext:10.6.2 0/0; EV2F-015: ext:3.13.1 0/0; EV2F-017: cap:5.2.1 0/0; EV2F-023: cap:8.3.2 0/0; EV2F-028: cla:3.1 0/0 |
| KG-Refinado | 4 | {'crudo=0,desc=0 (ausencia total)': 4} | EV2F-005: ext:4.6.1 0/0; EV2F-008: ext:10.6.2 0/0; EV2F-017: cap:5.2.1 0/0; EV2F-023: cap:8.3.2 0/0 |
| KG-Reextraído | 10 | {'crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)': 8, 'crudo>=1 (portador es contenedor >10 anclas)': 2} | EV2F-002: ext:5.10 0/13; EV2F-009: ext:5.7 0/19; EV2F-013: ext:3.17 1/51; EV2F-017: cap:5.2.1 0/16; EV2F-024: cap:2.11 0/28; EV2F-025: cla:2.1 0/21; EV2F-026: cla:3.5 0/10; EV2F-031: ric:7.2 1/0; EV2F-032: ric:9.2 0/7; EV2F-035: ric:5.2 0/10 |

## 4.b Sensibilidad (INFORMATIVA, fuera de la regla ratificada): ausencia_kg base con descendientes

INFORMATIVA, fuera de la regla ratificada: re-clasificación de las trazas base ausencia_kg resolviendo el ancla con incluir_descendientes=True (sub-puntos; contenedores excluidos). No reemplaza la clase primaria.

| grafo | id_pregunta | veredicto | nodos con descendientes | clase con descendientes |
|---|---|---|---|---|
| KG-Base | EV2F-005 | parcial | 0 | ausencia_kg |
| KG-Base | EV2F-008 | parcial | 0 | ausencia_kg |
| KG-Base | EV2F-015 | parcial | 0 | ausencia_kg |
| KG-Base | EV2F-017 | incorrecto | 0 | ausencia_kg |
| KG-Base | EV2F-023 | incorrecto | 0 | ausencia_kg |
| KG-Base | EV2F-028 | incorrecto | 0 | ausencia_kg |
| KG-Refinado | EV2F-005 | parcial | 0 | ausencia_kg |
| KG-Refinado | EV2F-008 | parcial | 0 | ausencia_kg |
| KG-Refinado | EV2F-017 | parcial | 0 | ausencia_kg |
| KG-Refinado | EV2F-023 | parcial | 0 | ausencia_kg |
| KG-Reextraído | EV2F-002 | parcial | 13 | generacion |
| KG-Reextraído | EV2F-009 | parcial | 19 | generacion |
| KG-Reextraído | EV2F-013 | parcial | 51 | generacion |
| KG-Reextraído | EV2F-017 | incorrecto | 16 | generacion |
| KG-Reextraído | EV2F-024 | parcial | 28 | generacion |
| KG-Reextraído | EV2F-025 | incorrecto | 21 | alcanzabilidad |
| KG-Reextraído | EV2F-026 | incorrecto | 10 | alcanzabilidad |
| KG-Reextraído | EV2F-031 | incorrecto | 0 | ausencia_kg |
| KG-Reextraído | EV2F-032 | parcial | 7 | generacion |

Reclasificación × grafo: {"run_3": {"ausencia_kg": 6}, "v3": {"ausencia_kg": 4}, "v2": {"generacion": 6, "alcanzabilidad": 2, "ausencia_kg": 1}}

## 5. Hallazgos numerados

Texto fijo incluido por `render_md` (los números salen de las tablas §1–§4 de
este mismo archivo, generadas por `atribucion_fallas.py --correr --incluir-enc
--sensibilidad-descendientes`; regla `regla_atribucion.md`, commit `40603a9`).
Nomenclatura: KG-Base (`12c226e2`) / KG-Refinado (`26fac8b4`) / KG-Reextraído (`8e2eadee`).

**H1 — Los 9-9 incorrectos NO son el mismo tipo de falla.** Sobre los pares
definitivos (§3.a, traza representativa): los 9 incorrectos de **KG-Refinado**
son 4 alcanzabilidad + 1 vista_no_consultada (5 de navegación: el ancla está y
el agente no la alcanzó u no la abrió), 2 generacion y 2 ausencia_kg (ambas
ausencias totales: `cap:5.2.1`, `cap:8.3.2`, 0/0 en §4). Los 9 de
**KG-Reextraído** son 4 ausencia_kg + 3 generacion + 1 alcanzabilidad + 1
vista_no_consultada: la mitad es "el ancla no resuelve" — y §4 muestra que 3 de
esas 4 anclas existen como sub-puntos (`cap:5.2.1` 16 descendientes, `cla:2.1`
21, `cla:3.5` 10) y la cuarta (`ric:7.2`) vive solo en un contenedor. Perfil:
KG-Refinado falla por navegación con el ancla presente; KG-Reextraído falla por
granularidad de ancla (la regla del censo la registra como ausencia) y por
generación. En las 120 trazas base (§1.b) el contraste es el mismo: incorrectos
KG-Refinado 0/3/1/2 (ausencia/alcanz./vista/generación) contra KG-Reextraído
4/0/1/3.

**H2 — KG-Base falla por navegación.** 8 de sus 17 incorrectos definitivos son
alcanzabilidad y 2 vista_no_consultada (10/17 de navegación; §3.b), más 4
ausencias totales (§4: 6 anclas de fidelidad no están en KG-Base en ninguna
forma, contra 4 en KG-Refinado y 0 totales en KG-Reextraído) y 3 generación.
En base (§1.a) KG-Base tiene 11 alcanzabilidad contra 6 y 1. Entre los
incorrectos definitivos la clase dominante es la navegación en KG-Base (10/17)
y en KG-Refinado (5/9), y la ausencia por granularidad en KG-Reextraído (4/9);
la generación no domina los incorrectos en ningún grafo (3, 2, 3). Coincide con
su recall consultada intermedio-bajo en navegabilidad y con sus 4 ausencias
totales del eje sintético.

**H3 — La generación es la clase mayoritaria de los parciales en los tres
grafos** (§1.b: 16/23, 23/30, 18/28 de los parciales base; §2.b: 37, 39, 39 de
las re-corridas parciales): cuando el agente llega al nodo-ancla, lo típico es
una respuesta parcial (tasa de criterios no cumplidos ≈ 0,48–0,59, la más baja
de las cuatro clases en cada grafo, tabla de criterios de §1), no una
incorrecta. Grounded ≠ correct sigue siendo el patrón dominante y es el mismo
en los tres grafos.

**H4 — Ausencia_kg significa cosas distintas en cada grafo.** En KG-Base y
KG-Refinado toda ancla no resuelta es ausencia total (crudo=0, desc=0: 6/6 y
4/4, §4). En KG-Reextraído 8/10 son granularidad (el punto existe solo como
sub-puntos) y 2/10 contenedor. La sensibilidad informativa de §4.b (fuera de
la regla ratificada) lo confirma: resolviendo con descendientes, las 9 trazas
base ausencia_kg de KG-Reextraído pasan a 6 generacion + 2 alcanzabilidad + 1
ausencia, mientras que las 6 de KG-Base y las 4 de KG-Refinado no se mueven.
Es coherente con la tasa de criterios no cumplidos de la clase ausencia_kg en
KG-Reextraído (0,72 base; **0,35** en las re-corridas §7, contra 0,61–0,87 en
los otros grafos): el agente encuentra el contenido en los sub-nodos aunque el
ancla exacta no exista. La clase primaria se mantiene por regla; la lectura del
mandato de la unidad anterior ("15/23 son granularidad") se replica en el eje
de fidelidad.

**H5 — Generación con abstención: el nodo-ancla consultado es cáscara.**
Generación × abstención (§1.c) = 1 / 2 / 4 en base. Los casos incorrectos de
ese cruce (EV2F-001 y EV2F-007 en ambos refinados, EV2F-011 en KG-Base,
EV2F-023 en KG-Reextraído; §3.b) son trazas en que el `ver_nodo` del ancla
devolvió un nodo con `properties` de encabezado o puntero (p. ej. `{"tipo":
"Enajenación de activos no financieros no producidos"}`; "Situaciones 13.3.1. a
13.3.9. que excepcionan…"; "deberán observar los siguientes requisitos") y el
agente, correctamente, declaró no encontrar el detalle. La regla clasifica
`generacion` porque el ancla fue consultada; el sub-diagnóstico "nodo-ancla sin
el contenido pedido" (defecto de profundidad de extracción, no de generación)
queda declarado como LIMITACIÓN de la clase y fuera del alcance de esta unidad
(`regla_atribucion.md` §7): es material para el verificador causal con laudo
humano, no para una quinta clase.

**H6 — Las re-corridas §7 replican el perfil base** (§2.a, 191 trazas):
generación 42/39/39, ausencia 8/12/18, alcanzabilidad 1/7/3,
vista_no_consultada 2/1/5. KG-Reextraído concentra las ausencias (18, todas
parciales), KG-Refinado la alcanzabilidad residual (7). No hay clase que
aparezca en las re-corridas y no en la base.

**H7 — Instrumento:** 120/120 (base) y 191/191 (§7) trazas con replay estándar
y fuerte OK (sha256 de los tres grafos verificados); doble corrida
byte-idéntica salvo `generado`; 7 re-corridas sin veredicto propio excluidas
y contadas; USD 0.

## Tabla por traza

Ver `atribucion_por_traza.md` (paquete de revisión) y `atribucion_fallas.json` → `base.por_traza` / `enc.por_traza` / `pares_definitivos.por_par`.
