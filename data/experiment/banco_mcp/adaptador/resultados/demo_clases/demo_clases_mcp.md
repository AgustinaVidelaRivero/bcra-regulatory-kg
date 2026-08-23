# Demostración por clase — U-A2.0-banco sobre MCP (entregable 7)

Casos: 19 | PASS: 18

| caso | contrato | ancla | veredicto | clase esperada | clase obtenida | presente | vista | consultada | replay | replay fuerte | determinismo | PASS/FAIL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GATE-01@A | v1 | ext:9.9 | incorrecto | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-02@A | v1 | ext:3.3 | parcial | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-03@A | v1 | ext:7.4 | incorrecto | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-04@A | v1 | ext:8.2 | parcial | vista_no_consultada | vista_no_consultada | True | True | False | True | True | True | PASS |
| GATE-05@A | v1 | ext:6.11 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-06@A | v1 | ext:6.11 | parcial | generacion | generacion | True | False | True | True | True | True | PASS |
| GATE-07@A | v1 | ext:6.11 | incorrecto | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-08@A | v1 | ext:6.11 | parcial | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-09@A | v1 | ext:6.11 | incorrecto | generacion | vista_no_consultada | True | True | False | True | True | True | PASS (detectado como no atribuible) |
| GATE-10@A | v1 | ext:10.1 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-01@B | v1 | ext:9.9 | incorrecto | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-02@B | v1 | ext:3.3 | parcial | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-03@B | v1 | ext:7.4 | incorrecto | alcanzabilidad | generacion | True | False | True | True | True | True | FAIL |
| GATE-04@B | v1 | ext:8.2 | parcial | vista_no_consultada | vista_no_consultada | True | True | False | True | True | True | PASS |
| GATE-05@B | v1 | ext:6.11 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-06@B | v1 | ext:6.11 | parcial | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-07@B | v1 | ext:6.11 | incorrecto | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-08@B | v1 | ext:6.11 | parcial | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-10@B | v1 | ext:10.1 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |

## Determinismo del adaptador

- re-adaptación desde la rebanada cruda: `ok = True` sobre 19 trazas (adaptación doble en memoria, JSON canónico salvo meta.generado)
- diferencias: []


## Lectura por criterio

| caso | maquinaria | clase |
|---|---|---|
| GATE-01@A | PASS | coincide |
| GATE-02@A | PASS | coincide |
| GATE-03@A | PASS | coincide |
| GATE-04@A | PASS | coincide |
| GATE-05@A | PASS | coincide |
| GATE-06@A | PASS | coincide |
| GATE-07@A | PASS | coincide |
| GATE-08@A | PASS | coincide |
| GATE-09@A | PASS (detectado como no atribuible) | n/a |
| GATE-10@A | PASS | coincide |
| GATE-01@B | PASS | coincide |
| GATE-02@B | PASS | coincide |
| GATE-03@B | PASS | difiere |
| GATE-04@B | PASS | coincide |
| GATE-05@B | PASS | coincide |
| GATE-06@B | PASS | coincide |
| GATE-07@B | PASS | coincide |
| GATE-08@B | PASS | coincide |
| GATE-10@B | PASS | coincide |

## No corridos

- GATE-11@A: contrato v2: fuera del banco (laudo R2, opción B); el servidor MCP no expone esa firma
