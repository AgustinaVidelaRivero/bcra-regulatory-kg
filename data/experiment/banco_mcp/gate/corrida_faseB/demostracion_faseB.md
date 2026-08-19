# Demostración por clase — U-A2.0-gate (entregable 5)

Casos: 9 | PASS: 8

| caso | contrato | ancla | veredicto | clase esperada | clase obtenida | presente | vista | consultada | replay | replay fuerte | determinismo | PASS/FAIL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GATE-01 | v1 | ext:9.9 | incorrecto | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-02 | v1 | ext:3.3 | parcial | ausencia_kg | ausencia_kg | False | False | False | True | True | True | PASS |
| GATE-03 | v1 | ext:7.4 | incorrecto | alcanzabilidad | generacion | True | False | True | True | True | True | FAIL |
| GATE-04 | v1 | ext:8.2 | parcial | vista_no_consultada | vista_no_consultada | True | True | False | True | True | True | PASS |
| GATE-05 | v1 | ext:6.11 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-06 | v1 | ext:6.11 | parcial | generacion | generacion | True | True | True | True | True | True | PASS |
| GATE-07 | v1 | ext:6.11 | incorrecto | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-08 | v1 | ext:6.11 | parcial | alcanzabilidad | alcanzabilidad | True | False | False | True | True | True | PASS |
| GATE-10 | v1 | ext:10.1 | incorrecto | generacion | generacion | True | True | True | True | True | True | PASS |

## Determinismo del adaptador

- re-adaptación desde la rebanada cruda: `ok = True` sobre 9 trazas (comparación byte a byte del JSON canónico salvo `meta.generado`)
- diferencias: []

