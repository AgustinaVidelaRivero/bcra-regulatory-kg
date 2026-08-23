# Censo de las 40 anclas de fidelidad de EV2 sobre KG-Reextraído-r1 (U-B1.8, fase A)

Generado 2026-08-23T17:21:42. Regla sellada del censo EV2 (sin cambios); columnas crudo/desc informativas (H24). Las filas de los tres grafos de EV2 se citan de la salida sellada de A0.2 (`85d9fdb`), no se recomputan.

- r1: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256 `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`
- contenedores (>10 anclas) en r1: 18; provenances sin parsear: 8

## Tabla comparativa (40 anclas por grafo)

| grafo | presentes | no resueltas | diagnóstico de las no resueltas |
|---|---|---|---|
| KG-Base (sellado) | 34 | 6 | {'crudo=0,desc=0 (ausencia total)': 6} |
| KG-Refinado (sellado) | 36 | 4 | {'crudo=0,desc=0 (ausencia total)': 4} |
| KG-Reextraído (sellado) | 30 | 10 | {'crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)': 8, 'crudo>=1 (portador es contenedor >10 anclas)': 2} |
| **KG-Reextraído-r1** | **31** | **9** | {'crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)': 7, 'crudo>=1 (portador es contenedor >10 anclas)': 2} |

## Anclas no resueltas en r1 (detalle)

| id_pregunta | ancla | crudo | desc | diagnóstico |
|---|---|---|---|---|
| EV2F-002 | ext:5.10 | 0 | 13 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-009 | ext:5.7 | 0 | 19 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-013 | ext:3.17 | 1 | 59 | crudo>=1 (portador es contenedor >10 anclas) |
| EV2F-017 | cap:5.2.1 | 0 | 16 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-024 | cap:2.11 | 0 | 28 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-025 | cla:2.1 | 0 | 21 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-031 | ric:7.2 | 1 | 0 | crudo>=1 (portador es contenedor >10 anclas) |
| EV2F-032 | ric:9.2 | 0 | 7 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |
| EV2F-035 | ric:5.2 | 0 | 10 | crudo=0,desc>0 (solo sub-puntos: granularidad de ancla) |

## Cambios de estado respecto de KG-Reextraído (sellado)

- `cap:2.11` (EV2F-024): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `cap:5.2.1` (EV2F-017): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `cla:2.1` (EV2F-025): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `cla:3.5` (EV2F-026): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → RESUELTA en r1 (n=1)
- `ext:3.17` (EV2F-013): no resuelta en KG-Reextraído [crudo>=1 (portador es contenedor >10 anclas)] → sigue no resuelta en r1 (crudo>=1 (portador es contenedor >10 anclas))
- `ext:5.10` (EV2F-002): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `ext:5.7` (EV2F-009): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `ric:5.2` (EV2F-035): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- `ric:7.2` (EV2F-031): no resuelta en KG-Reextraído [crudo>=1 (portador es contenedor >10 anclas)] → sigue no resuelta en r1 (crudo>=1 (portador es contenedor >10 anclas))
- `ric:9.2` (EV2F-032): no resuelta en KG-Reextraído [crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)] → sigue no resuelta en r1 (crudo=0,desc>0 (solo sub-puntos: granularidad de ancla))
- Sin regresiones: ninguna ancla presente en KG-Reextraído dejó de resolver en r1.

## Propuesta de umbral P1 (pre-registro §5; a laudo de la autora)

- Umbral pre-registrado: presentes(r1) ≥ 31/40 (no-resueltas ≤ 9, estrictamente menos que las 10 de KG-Reextraído).
- Observado: presentes(r1) = 31/40 (no-resueltas 9).
- Lectura mecánica contra el umbral: **dentro del umbral**. El veredicto formal de P1 se asienta en la tabla P1–P5 del cierre.
